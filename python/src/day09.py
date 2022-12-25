#!/usr/bin/env python3

from abstractsolver import AbstractSolver


class Solver(AbstractSolver):
    head_x = 0
    head_y = 0
    tail_x = 0
    tail_y = 0

    def read_input(self) -> None:
        pass

    def move_tail_1(self):
        # Head is directly 2 away from tail. Tail must move one towards head.
        if abs(self.head_x - self.tail_x) == 2 and self.head_y == self.tail_y:
            if self.head_x > self.tail_x:
                self.tail_x += 1
            else:
                self.tail_x -= 1
        elif abs(self.head_y - self.tail_y) == 2 and self.head_x == self.tail_x:
            if self.head_y > self.tail_y:
                self.tail_y += 1
            else:
                self.tail_y -= 1
        # Head and tail row and column are different, and they aren't touching.
        # Tail moves diagonally.
        elif abs(self.head_x - self.tail_x) == 2 and self.head_y != self.tail_y:
            if self.head_x > self.tail_x:
                self.tail_x += 1
            else:
                self.tail_x -= 1
            if self.head_y > self.tail_y:
                self.tail_y += 1
            else:
                self.tail_y -= 1
        elif abs(self.head_y - self.tail_y) == 2 and self.head_x != self.tail_x:
            if self.head_y > self.tail_y:
                self.tail_y += 1
            else:
                self.tail_y -= 1
            if self.head_x > self.tail_x:
                self.tail_x += 1
            else:
                self.tail_x -= 1

    def move_tail_2(self, head_x, head_y, tail_index):
        # Head is directly 2 away from tail. Tail must move one towards head.
        if (
            abs(head_x - self.tail_x[tail_index]) == 2
            and head_y == self.tail_y[tail_index]
        ):
            if head_x > self.tail_x[tail_index]:
                self.tail_x[tail_index] += 1
            else:
                self.tail_x[tail_index] -= 1
        elif (
            abs(head_y - self.tail_y[tail_index]) == 2
            and head_x == self.tail_x[tail_index]
        ):
            if head_y > self.tail_y[tail_index]:
                self.tail_y[tail_index] += 1
            else:
                self.tail_y[tail_index] -= 1
        # Head and tail row and column are different, and they aren't touching.
        # Tail moves diagonally.
        elif (
            abs(head_x - self.tail_x[tail_index]) == 2
            and head_y != self.tail_y[tail_index]
        ):
            if head_x > self.tail_x[tail_index]:
                self.tail_x[tail_index] += 1
            else:
                self.tail_x[tail_index] -= 1
            if head_y > self.tail_y[tail_index]:
                self.tail_y[tail_index] += 1
            else:
                self.tail_y[tail_index] -= 1
        elif (
            abs(head_y - self.tail_y[tail_index]) == 2
            and head_x != self.tail_x[tail_index]
        ):
            if head_y > self.tail_y[tail_index]:
                self.tail_y[tail_index] += 1
            else:
                self.tail_y[tail_index] -= 1
            if head_x > self.tail_x[tail_index]:
                self.tail_x[tail_index] += 1
            else:
                self.tail_x[tail_index] -= 1

    def solve1(self):
        all_tail_positions = {}
        all_tail_positions[(0, 0)] = True
        self.head_x = 0
        self.head_y = 0
        self.tail_x = 0
        self.tail_y = 0

        for line in self.input_lines:
            line_split = line.split()
            direction = line_split[0]
            amount = int(line_split[1])

            for i in range(0, amount):
                if direction == "R":
                    self.head_x += 1
                elif direction == "L":
                    self.head_x -= 1
                elif direction == "U":
                    self.head_y += 1
                elif direction == "D":
                    self.head_y -= 1
                else:
                    print("ERROR")
                    sys.exit(0)
                self.move_tail_1()
                all_tail_positions[(self.tail_x, self.tail_y)] = True

        return len(all_tail_positions)

    def solve2(self):
        all_tail_positions = {}
        all_tail_positions[(0, 0)] = True
        self.head_x = 0
        self.head_y = 0
        self.tail_x = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.tail_y = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        for line in self.input_lines:
            line_split = line.split()
            direction = line_split[0]
            amount = int(line_split[1])

            for i in range(0, amount):
                if direction == "R":
                    self.head_x += 1
                elif direction == "L":
                    self.head_x -= 1
                elif direction == "U":
                    self.head_y += 1
                elif direction == "D":
                    self.head_y -= 1
                else:
                    print("ERROR")
                    sys.exit(0)
                self.move_tail_2(self.head_x, self.head_y, 0)
                self.move_tail_2(self.tail_x[0], self.tail_y[0], 1)
                self.move_tail_2(self.tail_x[1], self.tail_y[1], 2)
                self.move_tail_2(self.tail_x[2], self.tail_y[2], 3)
                self.move_tail_2(self.tail_x[3], self.tail_y[3], 4)
                self.move_tail_2(self.tail_x[4], self.tail_y[4], 5)
                self.move_tail_2(self.tail_x[5], self.tail_y[5], 6)
                self.move_tail_2(self.tail_x[6], self.tail_y[6], 7)
                self.move_tail_2(self.tail_x[7], self.tail_y[7], 8)
                all_tail_positions[(self.tail_x[8], self.tail_y[8])] = True

        return len(all_tail_positions)
