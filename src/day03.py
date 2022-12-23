#!/usr/bin/env python3

from abstractsolver import AbstractSolver
import string


class Solver(AbstractSolver):
    def read_input(self) -> None:
        pass

    def solve1(self):
        score = 0
        for line in self.input_lines:
            full_line_len = len(line)
            half_line_len = int(full_line_len / 2)
            string1 = line[slice(0, half_line_len)]
            string2 = line[slice(half_line_len, full_line_len)]

            all_chars = string.ascii_lowercase + string.ascii_uppercase
            for i in range(0, 52):
                if all_chars[i] in string1 and all_chars[i] in string2:
                    score += i + 1

        return score

    def solve2(self):
        score = 0
        rucksacks = []
        for line in self.input_lines:
            rucksacks.append(line)

        num_rucksacks = len(rucksacks)
        all_chars = string.ascii_lowercase + string.ascii_uppercase

        for i in range(0, num_rucksacks, 3):
            for j in range(0, 52):
                if (
                    all_chars[j] in rucksacks[i]
                    and all_chars[j] in rucksacks[i + 1]
                    and all_chars[j] in rucksacks[i + 2]
                ):
                    score += j + 1

        return score
