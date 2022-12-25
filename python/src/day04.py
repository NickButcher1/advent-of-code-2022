#!/usr/bin/env python3

from abstractsolver import AbstractSolver


class Solver(AbstractSolver):
    def read_input(self) -> None:
        pass

    def solve1(self):
        score = 0
        for line in self.input_lines:
            split_line = line.split(",")
            one_start = int(split_line[0].split("-")[0])
            one_end = int(split_line[0].split("-")[1])
            two_start = int(split_line[1].split("-")[0])
            two_end = int(split_line[1].split("-")[1])

            if one_start >= two_start and one_end <= two_end:
                score += 1
            elif two_start >= one_start and two_end <= one_end:
                score += 1

        return score

    def solve2(self):
        score = 0
        for line in self.input_lines:
            split_line = line.split(",")
            one_start = int(split_line[0].split("-")[0])
            one_end = int(split_line[0].split("-")[1])
            two_start = int(split_line[1].split("-")[0])
            two_end = int(split_line[1].split("-")[1])

            if one_start < two_start:
                if one_end >= two_start:
                    score += 1
            elif one_start > two_start:
                if two_end >= one_start:
                    score += 1
            else:
                score += 1

        return score
