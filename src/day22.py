#!/usr/bin/env python3

from abstractsolver import AbstractSolver
import sys

VOID = 0
EMPTY = 1
WALL = 2

RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3


class Solver(AbstractSolver):
    num_rows: int
    num_cols: int
    matrix: list
    destinations: list
    directions: list
    record_route = False

    def print_matrix(self):
        print("MATRIX")
        for row in range(0, self.num_rows):
            output = ""
            for col in range(0, self.num_cols):
                content = self.matrix[row][col]
                if content == VOID:
                    output += " "
                elif content == EMPTY:
                    output += "."
                elif content == WALL:
                    output += "#"
                else:
                    output += content
            print(output)

    def print_destinations(self):
        print("DESTINATIONS")
        for row in range(0, self.num_rows):
            print(self.destinations[row])

    def read_input(self, lines: list) -> None:
        # Read number of rows and columns.
        self.num_cols = 0
        for line in lines:
            if len(line) > self.num_cols:
                self.num_cols = len(line)
            elif len(line) == 0:
                break
        self.num_rows = len(lines) - 2
        print("Num rows,cols: {},{}".format(self.num_rows, self.num_cols))

        # Read the map.
        self.matrix = []
        for line in lines:
            if len(line) == 0:
                break
            row = []
            self.matrix.append(row)
            for char in line:
                if char == " ":
                    row.append(VOID)
                elif char == ".":
                    row.append(EMPTY)
                elif char == "#":
                    row.append(WALL)
                else:
                    print("ERROR")
                    sys.exit(0)
            while len(row) < self.num_cols:
                row.append(VOID)

        self.print_matrix()

        # Read the directions.
        self.directions = []
        buffer = ""
        for char in lines[len(lines) - 1]:
            if char == "L" or char == "R":
                self.directions.append(int(buffer))
                buffer = ""
                self.directions.append(char)
            else:
                buffer += char
        if buffer != "":
            self.directions.append(int(buffer))
        # print("Directions: {}".format(self.directions))

    def calculate_destinations_part_2(self):
        self.destinations = []
        # TODO

    def calculate_destinations_part_1(self):
        self.destinations = []
        for row_idx in range(0, self.num_rows):
            row = []
            self.destinations.append(row)
            for col_idx in range(0, self.num_cols):
                row.append(None)

        for row_idx in range(0, self.num_rows):
            for col_idx in range(0, self.num_cols):
                content = self.matrix[row_idx][col_idx]
                if content == EMPTY:
                    targets = []
                    self.destinations[row_idx][col_idx] = targets

                    # RIGHT = 0
                    x = col_idx
                    while True:
                        x += 1
                        if x >= self.num_cols:
                            x = 0
                        if self.matrix[row_idx][x] == EMPTY:
                            targets.append((row_idx, x))
                            break
                        elif self.matrix[row_idx][x] == WALL:
                            targets.append((row_idx, col_idx))
                            break
                        # else VOID so try again.

                    # DOWN = 1
                    y = row_idx
                    while True:
                        y += 1
                        if y >= self.num_rows:
                            y = 0
                        if self.matrix[y][col_idx] == EMPTY:
                            targets.append((y, col_idx))
                            break
                        elif self.matrix[y][col_idx] == WALL:
                            targets.append((row_idx, col_idx))
                            break
                        # else VOID so try again.

                    # LEFT = 2
                    x = col_idx
                    while True:
                        x -= 1
                        if x == -1:
                            x = self.num_cols - 1
                        if self.matrix[row_idx][x] == EMPTY:
                            targets.append((row_idx, x))
                            break
                        elif self.matrix[row_idx][x] == WALL:
                            targets.append((row_idx, col_idx))
                            break
                        # else VOID so try again.

                    # UP = 3
                    y = row_idx
                    while True:
                        y -= 1
                        if y == -1:
                            y = self.num_rows - 1
                        if self.matrix[y][col_idx] == EMPTY:
                            targets.append((y, col_idx))
                            break
                        elif self.matrix[y][col_idx] == WALL:
                            targets.append((row_idx, col_idx))
                            break
                        # else VOID so try again.

        # self.print_destinations()

    def walk_from(self, starting_row, starting_col, starting_direction) -> int:
        print(
            "Walk from {},{} direction {}".format(
                starting_row, starting_col, starting_direction
            )
        )

        current_row = starting_row
        current_col = starting_col
        current_direction = starting_direction

        for direction in self.directions:
            if direction == "L":
                current_direction -= 1
                if current_direction == -1:
                    current_direction = 3
                # print("MOVE: TURN L TO FACE {}".format(current_direction))
            elif direction == "R":
                current_direction += 1
                if current_direction == 4:
                    current_direction = 0
                # print("MOVE: TURN R TO FACE {}".format(current_direction))
            else:
                # print("MOVE IN DIR {}, {} STEPS".format(current_direction, direction))
                for step in range(0, direction):
                    target = self.destinations[current_row][current_col]
                    new_position = target[current_direction]
                    if self.record_route:
                        if current_direction == RIGHT:
                            self.matrix[current_row][current_col] = ">"
                        elif current_direction == DOWN:
                            self.matrix[current_row][current_col] = "v"
                        elif current_direction == LEFT:
                            self.matrix[current_row][current_col] = "<"
                        elif current_direction == UP:
                            self.matrix[current_row][current_col] = "^"
                    current_row = new_position[0]
                    current_col = new_position[1]
            # print("Now at {},{} direction {}".format(current_row, current_col, current_direction))
            # self.print_matrix()

        self.print_matrix()
        # Add one to row and col before calculating answer (we use zero based, they use one).
        final_row = current_row + 1
        final_col = current_col + 1
        print(
            "Print final row,col {},{} direction {}".format(
                final_row, final_col, current_direction
            )
        )
        return 1000 * final_row + 4 * final_col + current_direction

    def solve_common(self) -> int:
        starting_row = 0
        starting_col = 0
        for x in self.matrix[0]:
            if x == EMPTY:
                break
            starting_col += 1
        return self.walk_from(starting_row, starting_col, RIGHT)

    def solve1(self):
        self.calculate_destinations_part_1()
        # self.record_route = True
        return self.solve_common()

    def solve2(self):
        self.calculate_destinations_part_2()
        self.record_route = True
        return self.solve_common()
