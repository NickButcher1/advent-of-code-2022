#!/usr/bin/env python3

from abstractsolver import AbstractSolver


class Solver(AbstractSolver):
    stacks = {}

    def init_stacks(self):
        # [G]                 [D] [R]
        # [W]         [V]     [C] [T] [M]
        # [L]         [P] [Z] [Q] [F] [V]
        # [J]         [S] [D] [J] [M] [T] [V]
        # [B]     [M] [H] [L] [Z] [J] [B] [S]
        # [R] [C] [T] [C] [T] [R] [D] [R] [D]
        # [T] [W] [Z] [T] [P] [B] [B] [H] [P]
        # [D] [S] [R] [D] [G] [F] [S] [L] [Q]
        #  1   2   3   4   5   6   7   8   9
        self.stacks[1] = ["G", "W", "L", "J", "B", "R", "T", "D"]
        self.stacks[2] = ["C", "W", "S"]
        self.stacks[3] = ["M", "T", "Z", "R"]
        self.stacks[4] = ["V", "P", "S", "H", "C", "T", "D"]
        self.stacks[5] = ["Z", "D", "L", "T", "P", "G"]
        self.stacks[6] = ["D", "C", "Q", "J", "Z", "R", "B", "F"]
        self.stacks[7] = ["R", "T", "F", "M", "J", "D", "B", "S"]
        self.stacks[8] = ["M", "V", "T", "B", "R", "H", "L"]
        self.stacks[9] = ["V", "S", "D", "P", "Q"]

    def read_input(self) -> None:
        pass

    def solve_common(self):
        self.init_stacks()

        for line in self.input_lines:
            split_line = line.split()
            move_number = int(split_line[1])
            move_from = int(split_line[3])
            move_to = int(split_line[5])

            if self.is_part_two:
                taken = []
                for i in range(0, move_number):
                    taken.append(self.stacks[move_from].pop(0))
                taken.reverse()

                for item in taken:
                    self.stacks[move_to].insert(0, item)
            else:
                for i in range(0, move_number):
                    taken = self.stacks[move_from].pop(0)
                    self.stacks[move_to].insert(0, taken)

        output = ""
        for i in range(1, 10):
            output += self.stacks[i][0]

        return output

    def solve1(self):
        return self.solve_common()

    def solve2(self):
        return self.solve_common()
