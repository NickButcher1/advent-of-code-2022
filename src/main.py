#!/usr/bin/env python3

import importlib
import sys
import time


def run_one_solver(day: int, use_real_input: bool, expected_outputs: list) -> None:
    start_time_ms = time.time()
    module_name = f"day{day:02}"
    input_file_name = f"../input/input{day:02}"
    if not use_real_input:
        input_file_name += "-sample"

    lines = []
    f = open(input_file_name)
    for line in f.readlines():
        lines.append(line.rstrip())
    f.close()

    day_module = importlib.import_module(module_name)
    solver = day_module.Solver(lines)
    solver.read_input()
    outputs = [solver.solve1()]
    solver.is_part_two = True
    outputs.append(solver.solve2())

    if expected_outputs != None:
        if (
            str(outputs[0]) != expected_outputs[0]
            or str(outputs[1]) != expected_outputs[1]
        ):
            print(
                "Day {} error:\n    Part one actual {} expected {}\n    Part two actual {} expected {}".format(
                    day,
                    outputs[0],
                    expected_outputs[0],
                    outputs[1],
                    expected_outputs[1],
                )
            )
            sys.exit(0)

    time_taken_ms = int(1000 * (time.time() - start_time_ms))
    print("Day {} {}ms\n{}\n{}".format(day, time_taken_ms, outputs[0], outputs[1]))
    return time_taken_ms


def read_expected_outputs() -> list:
    expected_outputs = []
    f = open("expected_outputs.txt")
    for line in f.readlines():
        expected_outputs.append(line.rstrip())
    f.close()

    if len(expected_outputs) != 50:
        print("Expected outputs file is wrong length: {}".format(len(expected_outputs)))
        sys.exit(0)
    return expected_outputs


# Command line parameters:
# 1  Day number.
# 2  Optional. Any value to use sample input instead of real input.
if __name__ == "__main__":
    use_real_input = len(sys.argv) != 3
    expected_outputs = read_expected_outputs()

    if sys.argv[1] == "all":
        total_time_taken_ms = 0
        for day in range(1, 26):
            total_time_taken_ms += run_one_solver(
                day, use_real_input, expected_outputs[day * 2 - 2 : day * 2]
            )
        print("Total time: {}ms".format(total_time_taken_ms))
    else:
        run_one_solver(int(sys.argv[1]), use_real_input, None)
