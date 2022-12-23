#!/usr/bin/env python3

from abc import ABC, abstractmethod


class AbstractSolver(ABC):
    is_part_two = False
    input_lines: list

    def __init__(self, input_lines):
        self.input_lines = input_lines

    @abstractmethod
    def read_input(self) -> None:
        ...

    @abstractmethod
    def solve1(self):
        ...

    @abstractmethod
    def solve2(self):
        ...
