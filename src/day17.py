#!/usr/bin/env python3

from abstractsolver import AbstractSolver
import sys

# Define the five shapes.
# Bottom left is (0,0)
class Shape:
    def __init__(self, solids):
        self.solids = solids


STARTING_ROWS = 5
MATRIX_WIDTH = 7


class Solver(AbstractSolver):
    matrix_rows = 0
    matrix = []

    # Start at the floor.
    highest_current_block = 0

    arrows = ""
    next_shape_idx = 0
    next_arrow_idx = 0

    shapes = [
        #  ####
        Shape([(0, 0), (1, 0), (2, 0), (3, 0)]),
        #   .#.
        #   ###
        #   .#.
        Shape([(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)]),
        #  ..#
        #  ..#
        #  ###
        Shape([(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]),
        #  #
        #  #
        #  #
        #  #
        Shape([(0, 0), (0, 1), (0, 2), (0, 3)]),
        #  ##
        #  ##
        Shape([(0, 0), (1, 0), (0, 1), (1, 1)]),
    ]

    def next_arrow(self):
        arrow = self.arrows[self.next_arrow_idx]
        self.next_arrow_idx += 1
        if self.next_arrow_idx % len(self.arrows) == 0:
            self.next_arrow_idx = 0
        return arrow

    def next_shape(self):
        shape = self.shapes[self.next_shape_idx]
        self.next_shape_idx += 1
        if self.next_shape_idx % 5 == 0:
            self.next_shape_idx = 0
        return shape

    def extend_matrix(self, by):
        self.matrix_rows += by
        for i in range(1, by + 1):
            self.matrix.append([".", ".", ".", ".", ".", ".", "."])

    def print_matrix(self):
        for i in range(self.matrix_rows - 1, 0, -1):
            output = "|"
            for j in range(0, MATRIX_WIDTH):
                output += self.matrix[i][j]
            output += "|"
            print(output)

        output = "+"
        for j in range(0, MATRIX_WIDTH):
            output += self.matrix[0][j]
        output += "+"
        print(output)
        print("\n")

    def move_left_if_possible(self, matrix, matrix_solids):
        for x, y in matrix_solids:
            if x == 0 or matrix[y][x - 1] == "#":
                return matrix_solids

        new_matrix_solids = []
        for x, y in matrix_solids:
            new_matrix_solids.append((x - 1, y))
        return new_matrix_solids

    def move_right_if_possible(self, matrix, matrix_solids):
        for x, y in matrix_solids:
            if x == (MATRIX_WIDTH - 1) or matrix[y][x + 1] == "#":
                return matrix_solids

        new_matrix_solids = []
        for x, y in matrix_solids:
            new_matrix_solids.append((x + 1, y))
        return new_matrix_solids

    def move_down_if_possible(self, matrix, matrix_solids):
        for x, y in matrix_solids:
            if y == 1 or matrix[y - 1][x] == "#":
                return (False, matrix_solids)

        new_matrix_solids = []
        for x, y in matrix_solids:
            new_matrix_solids.append((x, y - 1))
        return (True, new_matrix_solids)

    def copy_shape_into_matrix(self, matrix, matrix_solids):
        for x, y in matrix_solids:
            if y == 0 or matrix[y][x] == "#":
                print("ERROR")
                sys.exit(0)
            matrix[y][x] = "#"
            if y > self.highest_current_block:
                self.highest_current_block = y

    def drop_one_shape(self):
        shape = self.next_shape()

        while (self.matrix_rows - self.highest_current_block) < 8:
            self.extend_matrix(1)

        # Find starting position. Column is always fixed. Row is always a gap of 3 rows above the
        # previous top.
        # This is the bottom left of the imaginary square containing the shape.
        y_offset = self.highest_current_block + 4
        # Convert to matrix coordinates.
        matrix_solids = []
        for x, y in shape.solids:
            matrix_solids.append((x + 2, y + y_offset))

        moved_down = True
        while moved_down:
            arrow = self.next_arrow()
            if arrow == "<":
                matrix_solids = self.move_left_if_possible(self.matrix, matrix_solids)
            elif arrow == ">":
                matrix_solids = self.move_right_if_possible(self.matrix, matrix_solids)
            else:
                print("ERROR")
                sys.exit(0)

            moved_down, matrix_solids = self.move_down_if_possible(
                self.matrix, matrix_solids
            )

        self.copy_shape_into_matrix(self.matrix, matrix_solids)

    def read_input(self) -> None:
        for line in self.input_lines:
            self.arrows = line

    def solve_common(self):
        self.highest_current_block = 0
        self.matrix_rows = 1
        self.matrix = []
        self.matrix.append(["-", "-", "-", "-", "-", "-", "-"])
        self.extend_matrix(STARTING_ROWS)

    def solve1(self):
        self.solve_common()
        for i in range(0, 2022):
            self.drop_one_shape()
        return self.highest_current_block

    # PART TWO SOLUTION
    # FIRST ROW 141, REPEATS AT ROW 2689 and then 5237 (every 2548)
    #    |####...|
    #    |..###..|
    #    |...#...|
    #    |..####.|
    #    |..#....|
    #    |..#....|
    #    |###.#..| 141
    # 95 rocks gets the initial pattern in place, with highest as 141.
    #    |..#....| 143
    #    |..#....|
    #    |###.#..| 141
    # Anothter 1690 rocks gets the same pattern in place, with highest as 2691.
    #    |..#....| 2691 (143 + 2548)
    #    |..#....|
    #    |###.#..| 2689 (141 + 2548)
    # Anothter 1690 rocks gets the same pattern in place, with highest as 2691.
    #    |..#....| 5239 (143 + 2548 + 2548)
    #    |..#....|
    #    |###.#..| 5237 (141 + 2548 + 2548)
    def solve2(self):
        self.solve_common()
        return -1
