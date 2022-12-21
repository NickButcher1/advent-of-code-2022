#!/usr/bin/env python3

from abstractsolver import AbstractSolver
from abc import ABC, abstractmethod


class Monkey(ABC):
    def __init__(self, id, items):
        self.id = id
        self.items = items
        self.inspections = 0

    @abstractmethod
    def operation(self, old):
        pass

    @abstractmethod
    def test(self, level):
        pass


class Monkey0(Monkey):
    def operation(self, old):
        return old * 17

    def test(self, level):
        if (level % 3) == 0:
            return 3
        else:
            return 6


class Monkey1(Monkey):
    def operation(self, old):
        return old + 2

    def test(self, level):
        if (level % 13) == 0:
            return 3
        else:
            return 0


class Monkey2(Monkey):
    def operation(self, old):
        return old + 1

    def test(self, level):
        if (level % 2) == 0:
            return 0
        else:
            return 1


class Monkey3(Monkey):
    def operation(self, old):
        return old + 7

    def test(self, level):
        if (level % 11) == 0:
            return 6
        else:
            return 7


class Monkey4(Monkey):
    def operation(self, old):
        return old * old

    def test(self, level):
        if (level % 19) == 0:
            return 2
        else:
            return 5


class Monkey5(Monkey):
    def operation(self, old):
        return old + 8

    def test(self, level):
        if (level % 17) == 0:
            return 2
        else:
            return 1


class Monkey6(Monkey):
    def operation(self, old):
        return old * 2

    def test(self, level):
        if (level % 5) == 0:
            return 4
        else:
            return 7


class Monkey7(Monkey):
    def operation(self, old):
        return old + 6

    def test(self, level):
        if (level % 7) == 0:
            return 4
        else:
            return 5


class Solver(AbstractSolver):
    monkeys: list

    def read_input(self, lines: list) -> None:
        # Don't use the input file - I have hard coded the inputs.
        pass

    def init_monkeys(self) -> None:
        self.monkeys = [
            Monkey0(0, [59, 65, 86, 56, 74, 57, 56]),
            Monkey1(1, [63, 83, 50, 63, 56]),
            Monkey2(2, [93, 79, 74, 55]),
            Monkey3(3, [86, 61, 67, 88, 94, 69, 56, 91]),
            Monkey4(4, [76, 50, 51]),
            Monkey5(5, [77, 76]),
            Monkey6(6, [74]),
            Monkey7(7, [86, 85, 52, 86, 91, 95]),
        ]

    def calculate_score(self) -> int:
        scores = []
        for i in range(0, len(self.monkeys)):
            scores.append(self.monkeys[i].inspections)
        score1 = max(scores)
        scores.remove(score1)
        score2 = max(scores)
        return score1 * score2

    def solve_common(self, num_rounds):
        self.init_monkeys()

        for round_num in range(1, num_rounds):
            for i in range(0, len(self.monkeys)):
                monkey = self.monkeys[i]
                while len(monkey.items) != 0:
                    item = monkey.items.pop(0)
                    worry_level = monkey.operation(item)

                    if self.is_part_two:
                        worry_level_reduced = worry_level % 9699690
                    else:
                        worry_level_reduced = int(worry_level / 3)

                    next_monkey = monkey.test(worry_level_reduced)
                    monkey.inspections += 1
                    self.monkeys[next_monkey].items.append(worry_level_reduced)

        return self.calculate_score()

    def solve1(self):
        return self.solve_common(21)

    def solve2(self):
        return self.solve_common(10001)
