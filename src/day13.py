#!/usr/bin/env python3

from abstractsolver import AbstractSolver
import json
from functools import cmp_to_key


class Solver(AbstractSolver):
    input_lines: list

    def read_input(self, lines: list) -> None:
        self.input_lines = lines

    def packets_match(self, packet1, packet2):
        l1 = json.loads(packet1)
        l2 = json.loads(packet2)
        return self.lists_match(l1, l2)

    def lists_match(self, l1, l2):
        for i in range(0, min(len(l1), len(l2))):
            element1 = l1[i]
            element2 = l2[i]

            # If both values are integers, the lower integer should come first.
            # If the left integer is lower than the right integer, the inputs are in the right order.
            # If the left integer is higher than the right integer, the inputs are not in the right order.
            # Otherwise, the inputs are the same integer; continue checking the next part of the input.
            if isinstance(element1, int) and isinstance(element2, int):
                if element1 < element2:
                    # print("Exit TRUE  because element1 < element2")
                    return True
                elif element1 > element2:
                    # print("Exit FALSE because element1 > element2")
                    return False

            # If both values are lists, compare the first value of each list, then the second value, and so on.
            elif isinstance(element1, list) and isinstance(element2, list):
                rc = self.lists_match(element1, element2)
                if rc != "UNKNOWN":
                    return rc

            # If exactly one value is an integer, convert the integer to a list which contains that integer as its only value, then retry the comparison.
            # For example, if comparing [0,0,0] and 2, convert the right value to [2] (a list containing 2); the result is then found by instead comparing [0,0,0] and [2].
            elif isinstance(element1, int):
                element1 = [element1]
                rc = self.lists_match(element1, element2)
                if rc != "UNKNOWN":
                    return rc
            elif isinstance(element2, int):
                element2 = [element2]
                rc = self.lists_match(element1, element2)
                if rc != "UNKNOWN":
                    return rc
            else:
                print("ERROR")
                sys.exit(0)

        # If the left list runs out of items first, the inputs are in the right order.
        # If the right list runs out of items first, the inputs are not in the right order.
        # If the lists are the same length and no comparison makes a decision about the order, continue checking the next part of the input.
        if len(l1) < len(l2):
            return True
        elif len(l1) > len(l2):
            return False
        else:
            return "UNKNOWN"

    def solve1(self):
        sum_correct_pairs = 0
        pair_number = 0

        for i in range(0, len(self.input_lines), 3):
            pair_number += 1
            packet1 = self.input_lines[i]
            packet2 = self.input_lines[i + 1]

            if self.packets_match(packet1, packet2):
                sum_correct_pairs += pair_number

        return sum_correct_pairs

    def solve2(self):
        temp_lines = []

        for line in self.input_lines:
            if len(line) != 0:
                temp_lines.append(line)
        temp_lines.append("[[2]]")
        temp_lines.append("[[6]]")

        lines = []
        for line in temp_lines:
            lines.append(json.loads(line))

        def compare_lines(item1, item2):
            if self.lists_match(item1, item2):
                return 1
            else:
                return -1

        sorted_lines = sorted(lines, key=cmp_to_key(compare_lines), reverse=True)

        div2_idx = 0
        div6_idx = 0
        idx = 0
        for line in sorted_lines:
            idx += 1
            string_line = json.dumps(line)
            if string_line == "[[2]]":
                div2_idx = idx
            elif string_line == "[[6]]":
                div6_idx = idx
        return div6_idx * div2_idx
