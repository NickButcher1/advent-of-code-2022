#!/usr/bin/env python3

from abstractsolver import AbstractSolver

INT_TO_SNAFU = {-2: "=", -1: "-", 0: "0", 1: "1", 2: "2"}
SNAFU_TO_INT = {"=": -2, "-": -1, "0": 0, "1": 1, "2": 2}


class Solver(AbstractSolver):
    def read_input(self) -> None:
        pass

    def decimal_to_snafu(self, decimal: int) -> str:
        reverse_output = ""
        remaining_decimal = decimal

        while remaining_decimal != 0:
            remainder = remaining_decimal % 5
            remaining_decimal = int(remaining_decimal / 5)

            if remainder == 3:
                remainder = -2
                remaining_decimal += 1
            elif remainder == 4:
                remainder = -1
                remaining_decimal += 1
            reverse_output += INT_TO_SNAFU[remainder]
        return reverse_output[::-1]

    def snafu_to_decimal(self, snafu_str) -> int:
        mult = 1
        sum = 0
        for snafu_c in snafu_str[::-1]:
            sum += SNAFU_TO_INT[snafu_c] * mult
            mult *= 5
        return sum

    def solve1(self):
        sum = 0
        for line in self.input_lines:
            sum += self.snafu_to_decimal(line.split()[0])
        return self.decimal_to_snafu(sum)

    # There is no part two.
    def solve2(self):
        return -1
