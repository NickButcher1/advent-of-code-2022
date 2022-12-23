#!/usr/bin/env python3

from abstractsolver import AbstractSolver
import sys


class Solver(AbstractSolver):
    max_x: int
    max_y: int
    min_x: int
    min_y: int
    num_x: int
    num_y: int
    solution_found: bool

    def read_input(self) -> None:
        pass

    def print_grid(self, grid, num_x, num_y):
        for y in range(0, num_y):
            output = ""
            for x in range(0, num_x):
                output += grid[y][x]
            print(output)

        self.parse_input()

    def solve_common(self) -> int:
        min_x = 10000
        min_y = 10000
        max_x = 0
        max_y = 0

        for line in self.input_lines:
            snippets = line.split(" -> ")
            for snippet in snippets:
                x = int(snippet.split(",")[0])
                y = int(snippet.split(",")[1])
                if x < min_x:
                    min_x = x
                if x > max_x:
                    max_x = x
                if y < min_y:
                    min_y = y
                if y > max_y:
                    max_y = y

        if min_y > 0:
            min_y = 0

        if self.is_part_two:
            max_y += 2
            min_x = min_x - 200
            max_x = max_x + 200

        num_x = max_x - min_x + 1
        num_y = max_y - min_y + 1

        grid = []
        for y in range(0, num_y):
            row = []
            for x in range(0, num_x):
                row.append(".")
            grid.append(row)

        # Set sand.
        grid[0][500 - min_x] = "+"

        # Fill in all the lines.
        for line in self.input_lines:
            snippets = line.split(" -> ")
            for i in range(0, len(snippets) - 1):
                x1 = int(snippets[i].split(",")[0])
                y1 = int(snippets[i].split(",")[1])
                x2 = int(snippets[i + 1].split(",")[0])
                y2 = int(snippets[i + 1].split(",")[1])

                if x1 == x2:
                    if y2 < y1:
                        ytemp = y1
                        y1 = y2
                        y2 = ytemp
                    for y in range(y1, y2 + 1):
                        grid[y][x1 - min_x] = "#"
                elif y1 == y2:
                    if x2 < x1:
                        xtemp = x1
                        x1 = x2
                        x2 = xtemp
                    for x in range(x1, x2 + 1):
                        grid[y1][x - min_x] = "#"
                else:
                    print("ERROR")

        if self.is_part_two:
            for x in range(min_x, max_x + 1):
                grid[num_y - 1][x - min_x] = "#"

        num_sand = 0

        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y
        self.num_x = num_x
        self.num_y = num_y

        sand_x = 500
        sand_y = 0

        round_num = 0
        self.solution_found = False
        while True:
            while self.move_sand(grid, sand_x, sand_y) != "DONE":
                pass
            if self.solution_found:
                if self.is_part_two:
                    return round_num + 1
                else:
                    return round_num

            round_num += 1
            # print("ROUND: " + str(round_num) + " " + str(self.solution_found))
            # print_grid(grid, num_x, num_y)

    def move_sand(self, grid, sand_x, sand_y):
        if self.test_sand(grid, sand_x, sand_y + 1):
            # Move straight down one.
            return self.move_sand(grid, sand_x, sand_y + 1)
        elif self.test_sand(grid, sand_x - 1, sand_y + 1):
            # Move left and down one.
            return self.move_sand(grid, sand_x - 1, sand_y + 1)
        elif self.test_sand(grid, sand_x + 1, sand_y + 1):
            # Move right and down one.
            return self.move_sand(grid, sand_x + 1, sand_y + 1)
        else:
            # Can't move. Stop here.
            grid[sand_y][sand_x - self.min_x] = "o"

            if self.is_part_two:
                if sand_x == 500 and sand_y == 0:
                    self.solution_found = True

            return "DONE"

    # Return True if the test cell would accept sand.
    def test_sand(self, grid, sand_x, sand_y):
        if sand_y == self.num_y:
            # Can't drop on bottom.
            self.solution_found = True
        if (
            sand_y < self.num_y
            and sand_x >= self.min_x
            and sand_x < self.max_x
            and grid[sand_y][sand_x - self.min_x] == "."
        ):
            if sand_x == self.min_x and (
                grid[sand_y + 1][sand_x - self.min_x] == "o"
                or grid[sand_y + 1][sand_x - self.min_x] == "#"
            ):
                sys.exit(0)
            elif sand_x == self.max_x and (
                grid[sand_y + 1][sand_x - self.min_x] == "o"
                or grid[sand_y + 1][sand_x - self.min_x] == "#"
            ):
                sys.exit(0)
            else:
                return True
        else:
            return False

    def solve1(self):
        return self.solve_common()

    def solve2(self):
        return self.solve_common()
