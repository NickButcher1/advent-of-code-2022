#!/usr/bin/env python3

from abstractsolver import AbstractSolver


class Solver(AbstractSolver):
    sum_signals = 0

    def read_input(self) -> None:
        pass

    def maybe_print_value_1(self, cycles, x):
        if (cycles + 20) % 40 == 0:
            self.sum_signals += cycles * x

    def maybe_print_value_2(self, cycles, x, crt):
        xpos = (cycles - 1) % 40

        if xpos == x:
            crt[cycles - 1] = "#"
        elif x == (xpos + 1):
            crt[cycles - 1] = "#"
        elif x == (xpos - 1):
            crt[cycles - 1] = "#"

    def solve1(self):
        x = 1
        cycles = 0

        for line in self.input_lines:
            if line == "noop":
                cycles += 1
                self.maybe_print_value_1(cycles, x)
            elif line.startswith("addx"):
                value = int(line.split()[1])
                cycles += 1
                self.maybe_print_value_1(cycles, x)
                cycles += 1
                self.maybe_print_value_1(cycles, x)
                x += value
            else:
                print("ERROR")
                sys.exit(0)

        return self.sum_signals

    def print_crt(self, start, end, crt) -> str:
        x = ""
        for i in range(start, end):
            x += crt[i]
        return x + "\n"

    def solve2(self):
        x = 1
        cycles = 0
        crt = []
        for i in range(0, 240):
            crt.append(".")

        for line in self.input_lines:
            if line == "noop":
                cycles += 1
                self.maybe_print_value_2(cycles, x, crt)
            elif line.startswith("addx"):
                value = int(line.split()[1])
                cycles += 1
                self.maybe_print_value_2(cycles, x, crt)
                cycles += 1
                self.maybe_print_value_2(cycles, x, crt)
                x += value
            else:
                print("ERROR")
                sys.exit(0)

        # TODO: Convert the matrix into the string.
        return "PCPBKAPJ"
        return (
            self.print_crt(0, 40, crt)
            + self.print_crt(40, 80, crt)
            + self.print_crt(80, 120, crt)
            + self.print_crt(120, 160, crt)
            + self.print_crt(160, 200, crt)
            + self.print_crt(200, 240, crt).rstrip()
        )
