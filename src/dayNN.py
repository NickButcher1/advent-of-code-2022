#!/usr/bin/env python3

from abstractsolver import AbstractSolver


class Solver(AbstractSolver):
    input_lines: list

    def read_input(self, lines: list) -> None:
        # TODO: Process the input.
        self.input_lines = lines

    def solve1(self) -> int:
        return -1

    def solve2(self) -> int:
        return -1
