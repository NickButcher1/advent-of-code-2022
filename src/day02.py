#!/usr/bin/env python3

from abstractsolver import AbstractSolver


class Solver(AbstractSolver):
    inputs = []

    def read_input(self, lines: list) -> None:
        for line in lines:
            x = line[0]
            y = line[2]
            z = line[0] + line[2]
            self.inputs.append(z)

    def solve_common(self, lookup_table: dict) -> int:
        score = 0

        for input in self.inputs:
            score += lookup_table[input]

        return score

    def solve1(self):
        lookup_table = {}
        # Rock
        lookup_table["AX"] = 1 + 3
        lookup_table["AY"] = 2 + 6
        lookup_table["AZ"] = 3 + 0
        # Paper
        lookup_table["BX"] = 1 + 0
        lookup_table["BY"] = 2 + 3
        lookup_table["BZ"] = 3 + 6
        # Scissors
        lookup_table["CX"] = 1 + 6
        lookup_table["CY"] = 2 + 0
        lookup_table["CZ"] = 3 + 3

        return self.solve_common(lookup_table)

    def solve2(self):
        # X=LOSE, Y=DRAW, Z=WIN
        lookup_table = {}
        # Rock
        lookup_table["AX"] = 3 + 0
        lookup_table["AY"] = 1 + 3
        lookup_table["AZ"] = 2 + 6
        # Paper
        lookup_table["BX"] = 1 + 0
        lookup_table["BY"] = 2 + 3
        lookup_table["BZ"] = 3 + 6
        # Scissors
        lookup_table["CX"] = 2 + 0
        lookup_table["CY"] = 3 + 3
        lookup_table["CZ"] = 1 + 6

        return self.solve_common(lookup_table)
