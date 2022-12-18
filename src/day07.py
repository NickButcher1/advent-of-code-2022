#!/usr/bin/env python3

from abstractsolver import AbstractSolver
import string

TOTAL_DISK = 70000000
NEED_UNUSED = 30000000


class Direct:
    def __init__(self, name, previous):
        self.name = name
        self.previous = previous
        self.entries = {}
        self.fileSizes = 0


class Solver(AbstractSolver):
    input_lines: list
    root_dir = Direct("ROOT", None)
    current_dir = root_dir
    in_listing = False
    total_inclusive_size_here = 0
    all_dirs = []

    def process_line(self, line):
        if line == "$ cd /":
            self.current_dir = self.root_dir
        elif line == "$ cd ..":
            self.current_dir = self.current_dir.previous
        elif line == "$ ls":
            self.in_listing = True
        elif line.startswith("$ cd "):
            new_dir_name = line.split()[2]
            self.current_dir = self.current_dir.entries[new_dir_name]

    def print_dict(self, input_direct, indent) -> int:
        size_here = 0
        for key in input_direct.entries.keys():
            size_here += self.print_dict(input_direct.entries[key], indent + "  ")
        inclusive_size_here = size_here + input_direct.fileSizes
        if inclusive_size_here <= 100000:
            self.total_inclusive_size_here += inclusive_size_here

        self.all_dirs.append((inclusive_size_here, input_direct.name))
        return size_here + input_direct.fileSizes

    def read_input(self, lines: list) -> None:
        self.input_lines = lines

    def solve_common(self):
        self.total_inclusive_size_here = 0

        for line in self.input_lines:
            if self.in_listing:
                if line[0].isdigit():
                    new_size = int(line.split()[0])
                    self.current_dir.fileSizes += new_size
                elif line[0] == "d":
                    new_dir_name = line.split()[1]
                    new_direct = Direct(new_dir_name, self.current_dir)
                    self.current_dir.entries[new_dir_name] = new_direct
                else:
                    self.in_listing = False
                    self.process_line(line)
            else:
                self.process_line(line)

    def solve1(self):
        self.solve_common()
        self.print_dict(self.root_dir, "")
        return self.total_inclusive_size_here

    def solve2(self):
        self.solve_common()
        root_size = self.print_dict(self.root_dir, "")

        current_free = TOTAL_DISK - root_size
        need_to_delete = NEED_UNUSED - current_free

        self.all_dirs.sort()
        for x in self.all_dirs:
            if x[0] > need_to_delete:
                return x[0]
