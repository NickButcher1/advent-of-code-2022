#!/usr/bin/env python3

from abstractsolver import AbstractSolver


class Solver(AbstractSolver):
    input_lines: list

    def read_input(self, lines: list) -> None:
        # No need to process the input.
        self.input_lines = lines

    def solve1(self) -> int:
        current_sum = 0
        max_sum = 0

        for line in self.input_lines:
            if len(line) == 0:
                if current_sum > max_sum:
                    max_sum = current_sum
                current_sum = 0
            else:
                intval = int(line)
                current_sum += intval

        return max_sum

    def solve2(self) -> str:
        current_sum = 0
        max_sums = []

        for line in self.input_lines:
            if len(line) == 0:
                max_sums.append(current_sum)
                current_sum = 0
            else:
                intval = int(line)
                current_sum += intval

        max_sums.sort()
        max_sums.reverse()
        return max_sums[0] + max_sums[1] + max_sums[2]
