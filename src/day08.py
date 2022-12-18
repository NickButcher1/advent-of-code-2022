#!/usr/bin/env python3

from abstractsolver import AbstractSolver
import string


class Solver(AbstractSolver):
    num_per_row = 0
    matrix = []

    def read_input(self, lines: list) -> None:
        for line in lines:
            self.num_per_row = len(line)
            row = []
            for i in range(0, len(line)):
                row.append(int(line[i]))
            self.matrix.append(row)

    def solve1(self):
        visible_count = 4 * (self.num_per_row - 1)

        for x in range(1, self.num_per_row - 1):
            for y in range(1, self.num_per_row - 1):
                value = self.matrix[x][y]
                is_visible_a = True
                for xx in range(0, x):
                    if self.matrix[xx][y] >= value:
                        is_visible_a = False

                is_visible_b = True
                for xx in range(x + 1, self.num_per_row):
                    if self.matrix[xx][y] >= value:
                        is_visible_b = False

                is_visible_c = True
                for yy in range(0, y):
                    if self.matrix[x][yy] >= value:
                        is_visible_c = False

                is_visible_d = True
                for yy in range(y + 1, self.num_per_row):
                    if self.matrix[x][yy] >= value:
                        is_visible_d = False

                if is_visible_a or is_visible_b or is_visible_c or is_visible_d:
                    visible_count += 1

        return visible_count

    def solve2(self):
        visible_count = 4 * (self.num_per_row - 1)
        best_score = 0

        for x in range(1, self.num_per_row - 1):
            for y in range(1, self.num_per_row - 1):
                value = self.matrix[x][y]

                score_a = 0
                for xx in range(x - 1, -1, -1):
                    score_a += 1
                    if self.matrix[xx][y] >= value:
                        break

                score_b = 0
                for xx in range(x + 1, self.num_per_row, 1):
                    score_b += 1
                    if self.matrix[xx][y] >= value:
                        break

                score_c = 0
                for yy in range(y - 1, -1, -1):
                    score_c += 1
                    if self.matrix[x][yy] >= value:
                        break

                score_d = 0
                for yy in range(y + 1, self.num_per_row, 1):
                    score_d += 1
                    if self.matrix[x][yy] >= value:
                        break

                score_total = score_a * score_b * score_c * score_d
                if score_total >= best_score:
                    best_score = score_total

        return best_score
