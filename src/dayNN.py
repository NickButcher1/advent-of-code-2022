#!/usr/bin/env python3

from abstractsolver import AbstractSolver


class Solver(AbstractSolver):
    input_lines: list

    def read_input(self, lines: list) -> None:
        self.input_lines = lines

    def solve1(self):
        return -1

    def solve2(self):
        return -1
