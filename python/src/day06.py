#!/usr/bin/env python3

from abstractsolver import AbstractSolver


class Solver(AbstractSolver):
    def is_unique(self, input):
        dict1 = {}
        for i in range(0, len(input)):
            if input[i] in dict1.keys():
                return False
            else:
                dict1[input[i]] = 1
        return True

    def read_input(self) -> None:
        pass

    def solve_common(self, idx: int):
        for line in self.input_lines:
            for i in range(0, len(line)):
                if self.is_unique(line[i : i + idx]):
                    return i + idx

    def solve1(self):
        return self.solve_common(4)

    def solve2(self):
        return self.solve_common(14)
