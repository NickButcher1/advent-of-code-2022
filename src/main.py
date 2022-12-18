#!/usr/bin/env python3

import importlib
import sys


def main(day: int, real_data: bool) -> None:
    module_name = f"day{day:02}"
    input_file_name = f"../input/input{day:02}"
    if not real_data:
        input_file_name += "-sample"

    lines = []
    f = open(input_file_name)
    for line in f.readlines():
        lines.append(line.rstrip())
    f.close()

    day_module = importlib.import_module(module_name)
    solver = day_module.Solver()
    solver.read_input(lines)
    print(solver.solve1())
    print(solver.solve2())


# Command line parameters:
# 1  Day number.
# 2  Optional. Any value to use sample input instead of real input.
if __name__ == "__main__":
    main(int(sys.argv[1]), len(sys.argv) != 3)
