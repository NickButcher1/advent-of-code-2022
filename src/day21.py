#!/usr/bin/env python3

from abstractsolver import AbstractSolver
import sys

# A lone number means the monkey's job is simply to yell that number.
# A job like aaaa + bbbb means the monkey waits for monkeys aaaa and bbbb to yell each of their numbers; the monkey then yells the sum of those two numbers.
# aaaa - bbbb means the monkey yells aaaa's number minus bbbb's number.
# Job aaaa * bbbb will yell aaaa's number multiplied by bbbb's number.
# Job aaaa / bbbb will yell aaaa's number divided by bbbb's number.


class Solver(AbstractSolver):
    numbers_dict = {}
    todo_dict = {}
    original_numbers_dict = {}
    original_todo_dict = {}

    def copy_dict(self, src_dict, target_dict):
        target_dict.clear()
        for key in src_dict.keys():
            target_dict[key] = src_dict[key]

    def read_input(self) -> None:
        for line in self.input_lines:
            monkey_name = line.split(":")[0]
            line_split = line.split()

            if len(line_split) == 2:
                self.numbers_dict[monkey_name] = int(line_split[1])
            else:
                self.todo_dict[monkey_name] = (
                    line_split[1],
                    line_split[2],
                    line_split[3],
                )
        self.copy_dict(self.numbers_dict, self.original_numbers_dict)
        self.copy_dict(self.todo_dict, self.original_todo_dict)

    def result_for(self, numbers_dict, a, operation, b) -> int:
        result = -1

        if operation == "+":
            result = numbers_dict[a] + numbers_dict[b]
        elif operation == "-":
            result = numbers_dict[a] - numbers_dict[b]
        elif operation == "*":
            result = numbers_dict[a] * numbers_dict[b]
        elif operation == "/":
            result = numbers_dict[a] / numbers_dict[b]

        return result

    def solve1(self):
        while True:
            for monkey_name in self.todo_dict.copy().keys():
                a, operation, b = self.todo_dict[monkey_name]
                if a in self.numbers_dict and b in self.numbers_dict:
                    result = self.result_for(self.numbers_dict, a, operation, b)

                    if result != -1:
                        del self.todo_dict[monkey_name]
                        if monkey_name == "root":
                            return int(result)
                        self.numbers_dict[monkey_name] = result

    def partial_solve_without_humn(self, numbers_dict, todo_dict):
        """Optimisation, which solves as far as possible without knowing the value for "humn"."""
        del numbers_dict["humn"]
        del todo_dict["root"]

        prev_todo_len = len(todo_dict)
        while True:
            for monkey_name in todo_dict.copy().keys():
                a, operation, b = todo_dict[monkey_name]
                if a in numbers_dict and b in numbers_dict:
                    result = self.result_for(numbers_dict, a, operation, b)

                    if result != -1:
                        del todo_dict[monkey_name]
                        if monkey_name == "root":
                            return result
                        numbers_dict[monkey_name] = result
            if prev_todo_len == len(todo_dict):
                # Prevent getting stuck.
                return
            prev_todo_len = len(todo_dict)

    def solve2(self):
        self.copy_dict(self.original_numbers_dict, self.numbers_dict)
        self.copy_dict(self.original_todo_dict, self.todo_dict)
        root_monkey = self.todo_dict["root"]
        self.partial_solve_without_humn(
            self.original_numbers_dict, self.original_todo_dict
        )

        # The RHS of root is a fixed value, in both the sample and actual input. While this is not
        # stated in the description, assume this is always true.
        #
        # In the sample, the LHS increases with increasing "humn".
        # In the actual input, the LHS decreases with increasing "humn".
        # Therefore this method only works for the actual input. To make it work for the sample,
        # invert the `root_lhs > root_rhs` test below.
        humn_min = 0
        humn_max = 1000000000000000000000000000000

        while len(self.todo_dict) != 0:
            humn = int((humn_min + humn_max) / 2)

            self.numbers_dict["humn"] = humn
            self.todo_dict["root"] = (root_monkey[0], "=", root_monkey[2])

            prev_todo_len = len(self.todo_dict)
            while True:
                for monkey_name in self.todo_dict.copy().keys():
                    a, operation, b = self.todo_dict[monkey_name]
                    if a in self.numbers_dict and b in self.numbers_dict:
                        result = -1
                        if operation == "=":
                            if self.numbers_dict[a] == self.numbers_dict[b]:
                                result = humn
                        else:
                            result = self.result_for(self.numbers_dict, a, operation, b)

                        if result != -1:
                            del self.todo_dict[monkey_name]
                            if monkey_name == "root":
                                return humn
                            self.numbers_dict[monkey_name] = result
                if (
                    self.todo_dict["root"][0] in self.numbers_dict
                    and self.todo_dict["root"][2] in self.numbers_dict
                ):
                    root_lhs = self.numbers_dict[self.todo_dict["root"][0]]
                    root_rhs = self.numbers_dict[self.todo_dict["root"][2]]
                    if root_lhs != root_rhs:
                        if root_lhs > root_rhs:
                            humn_min = humn
                        else:
                            humn_max = humn
                        break
                if prev_todo_len == len(self.todo_dict):
                    # Prevent getting stuck.
                    break
                prev_todo_len = len(self.todo_dict)

            self.copy_dict(self.original_numbers_dict, self.numbers_dict)
            self.copy_dict(self.original_todo_dict, self.todo_dict)
