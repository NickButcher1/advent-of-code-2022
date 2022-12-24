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

    right_from = []
    down_from = []
    left_from = []
    up_from = []

    record_route = False

    def print_matrix(self):
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

    def read_input(self) -> None:
        # Read number of rows and columns.
        self.num_cols = 0
        for line in self.input_lines:
            if len(line) > self.num_cols:
                self.num_cols = len(line)
            elif len(line) == 0:
                break
        self.num_rows = len(self.input_lines) - 2

        # Read the map.
        self.matrix = []
        for line in self.input_lines:
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

        # Read the directions.
        self.directions = []
        buffer = ""
        for char in self.input_lines[len(self.input_lines) - 1]:
            if char == "L" or char == "R":
                self.directions.append(int(buffer))
                buffer = ""
                self.directions.append(char)
            else:
                buffer += char
        if buffer != "":
            self.directions.append(int(buffer))

    def calculate_destinations_common(self):
        self.destinations = []
        for row_idx in range(0, self.num_rows):
            row = []
            self.destinations.append(row)
            for col_idx in range(0, self.num_cols):
                row.append(None)

    def init_from_list(self, from_list):
        for row_idx in range(0, self.num_rows):
            row = []
            from_list.append(row)
            for col_idx in range(0, self.num_cols):
                row.append(None)

    def calculate_destinations_part_2(self):
        self.calculate_destinations_common()

        self.init_from_list(self.right_from)
        self.init_from_list(self.down_from)
        self.init_from_list(self.left_from)
        self.init_from_list(self.up_from)

        # Edge Facing  -> Edge Facing

        #    1     UP       10  RIGHT
        for i in range(0, 50):
            self.up_from[0][i + 50] = (i + 150, 0, RIGHT)

        #    2     UP        6     UP
        for i in range(0, 50):
            self.up_from[0][i + 100] = (199, i + 0, UP)

        #    3     UP        8  RIGHT
        for i in range(0, 50):
            self.up_from[100][i + 0] = (i + 50, 50, RIGHT)

        #    4   DOWN       12   LEFT
        for i in range(0, 50):
            self.down_from[49][100 + i] = (50 + i, 99, LEFT)

        #    5   DOWN       14   LEFT
        for i in range(0, 50):
            self.down_from[149][i + 50] = (150 + i, 49, LEFT)

        #    6   DOWN        2   DOWN
        for i in range(0, 50):
            self.down_from[199][i + 0] = (0, 100 + i, DOWN)

        #    7   LEFT        9  RIGHT
        for i in range(0, 50):
            self.left_from[i + 0][50] = (149 - i, 0, RIGHT)

        #    8   LEFT        3   DOWN
        for i in range(0, 50):
            self.left_from[50 + i][50] = (100, i + 0, DOWN)

        #    9   LEFT        7  RIGHT
        for i in range(0, 50):
            self.left_from[100 + i][0] = (49 - i, 50, RIGHT)

        #   10   LEFT        1   DOWN
        for i in range(0, 50):
            self.left_from[150 + i][0] = (0, 50 + i, DOWN)

        #   11  RIGHT       13   LEFT
        for i in range(0, 50):
            self.right_from[i + 0][149] = (149 - i, 99, LEFT)

        #   12  RIGHT        4     UP
        for i in range(0, 50):
            self.right_from[50 + i][99] = (49, 100 + i, UP)

        #   13  RIGHT       11   LEFT
        for i in range(0, 50):
            self.right_from[100 + i][99] = (49 - i, 149, LEFT)

        #   14  RIGHT        5     UP
        for i in range(0, 50):
            self.right_from[150 + i][49] = (149, 50 + i, UP)

        for row_idx in range(0, self.num_rows):
            for col_idx in range(0, self.num_cols):
                content = self.matrix[row_idx][col_idx]
                if content == EMPTY:
                    targets = []
                    self.destinations[row_idx][col_idx] = targets

                    # RIGHT = 0
                    dest = self.right_from[row_idx][col_idx]
                    if dest is None:
                        x = col_idx + 1
                        y = row_idx
                        d = -1
                    else:
                        y, x, d = dest
                    if self.matrix[y][x] == EMPTY:
                        targets.append((y, x, d))
                    elif self.matrix[y][x] == WALL:
                        targets.append((row_idx, col_idx, d))
                    else:
                        print("ERROR-R x={}".format(x))
                        sys.exit(0)

                    # DOWN = 1
                    dest = self.down_from[row_idx][col_idx]
                    if dest is None:
                        y = row_idx + 1
                        x = col_idx
                        d = -1
                    else:
                        y, x, d = dest
                    if self.matrix[y][x] == EMPTY:
                        targets.append((y, x, d))
                    elif self.matrix[y][x] == WALL:
                        targets.append((row_idx, col_idx, d))
                    else:
                        print("ERROR-D y={}".format(y))
                        sys.exit(0)

                    # LEFT = 2
                    dest = self.left_from[row_idx][col_idx]
                    if dest is None:
                        x = col_idx - 1
                        y = row_idx
                        d = -1
                    else:
                        y, x, d = dest
                    if self.matrix[y][x] == EMPTY:
                        targets.append((y, x, d))
                    elif self.matrix[y][x] == WALL:
                        targets.append((row_idx, col_idx, d))
                    else:
                        print("ERROR-L x={}".format(x))
                        sys.exit(0)

                    # UP = 3
                    dest = self.up_from[row_idx][col_idx]
                    if dest is None:
                        y = row_idx - 1
                        x = col_idx
                        d = -1
                    else:
                        y, x, d = dest
                    if self.matrix[y][x] == EMPTY:
                        targets.append((y, x, d))
                    elif self.matrix[y][x] == WALL:
                        targets.append((row_idx, col_idx, d))
                    else:
                        print("ERROR-U y={}".format(y))
                        sys.exit(0)

    def calculate_destinations_part_1(self):
        self.calculate_destinations_common()

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

    def walk_from(self, starting_row, starting_col, starting_direction) -> int:
        current_row = starting_row
        current_col = starting_col
        current_direction = starting_direction

        for direction in self.directions:
            if direction == "L":
                current_direction -= 1
                if current_direction == -1:
                    current_direction = 3
            elif direction == "R":
                current_direction += 1
                if current_direction == 4:
                    current_direction = 0
            else:
                for step in range(0, direction):
                    target = self.destinations[current_row][current_col]

                    new_position = target[current_direction]
                    if self.is_part_two:
                        new_direction = new_position[2]

                    if self.record_route:
                        if current_direction == RIGHT:
                            self.matrix[current_row][current_col] = ">"
                        elif current_direction == DOWN:
                            self.matrix[current_row][current_col] = "v"
                        elif current_direction == LEFT:
                            self.matrix[current_row][current_col] = "<"
                        elif current_direction == UP:
                            self.matrix[current_row][current_col] = "^"

                    if self.is_part_two:
                        if new_direction != -1 and (
                            current_row != new_position[0]
                            or current_col != new_position[1]
                        ):
                            current_direction = new_direction
                    current_row = new_position[0]
                    current_col = new_position[1]

        # Add one to row and col before calculating answer (we use zero based, they use one).
        final_row = current_row + 1
        final_col = current_col + 1
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
        return self.solve_common()

    def solve2(self):
        self.calculate_destinations_part_2()
        self.record_route = True
        return self.solve_common()
