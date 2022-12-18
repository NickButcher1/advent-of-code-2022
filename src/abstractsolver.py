#!/usr/bin/env python3

from abc import ABC, abstractmethod


class AbstractSolver(ABC):
    @abstractmethod
    def read_input(input_lines: list) -> None:
        ...

    @abstractmethod
    def solve1():
        ...

    @abstractmethod
    def solve2():
        ...
