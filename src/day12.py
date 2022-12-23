#!/usr/bin/env python3

from abstractsolver import AbstractSolver


class Solver(AbstractSolver):
    valid_moves: list
    visited: list
    start_x = -1
    start_y = -1
    end_x = -1
    end_y = -1
    num_rows = 0
    num_cols = 0
    start_points_for_part_two = []

    def read_input(self) -> None:
        matrix = []
        y = 0

        for line in self.input_lines:
            self.num_cols = len(line)
            row = []
            for i in range(0, len(line)):
                value = line[i]
                if value == "S":
                    self.start_x = y
                    self.start_y = i
                    value = 1
                elif value == "E":
                    self.end_x = y
                    self.end_y = i
                    value = 26
                else:
                    if value == "a":
                        self.start_points_for_part_two.append((y, i))
                    value = ord(value) - ord("a") + 1
                row.append(value)
            matrix.append(row)
            y += 1
        self.num_rows = y

        self.reset_visited()

        self.valid_moves = []
        for row in range(0, self.num_rows):
            self.valid_moves.append([])
            for col in range(0, self.num_cols):
                self.valid_moves[row].append(None)

        for row in range(0, self.num_rows):
            for col in range(0, self.num_cols):
                valid_here = []
                # UP
                if row != 0:
                    if matrix[row - 1][col] - matrix[row][col] <= 1:
                        valid_here.append((row - 1, col))
                # DOWN
                if row != (self.num_rows - 1):
                    if matrix[row + 1][col] - matrix[row][col] <= 1:
                        valid_here.append((row + 1, col))
                # LEFT
                if col != 0:
                    if matrix[row][col - 1] - matrix[row][col] <= 1:
                        valid_here.append((row, col - 1))
                # RIGHT
                if col != (self.num_cols - 1):
                    if matrix[row][col + 1] - matrix[row][col] <= 1:
                        valid_here.append((row, col + 1))

                self.valid_moves[row][col] = valid_here

    def reset_visited(self):
        self.visited = []
        for row in range(0, self.num_rows):
            self.visited.append([])
            for col in range(0, self.num_cols):
                self.visited[row].append("NO")

    def calculate_cell(self, depth, row, col):
        for move_row, move_col in self.valid_moves[row][col]:
            if self.visited[move_row][move_col] == "NO":
                self.visited[move_row][move_col] = depth + 1

    def solve_for_start_point(self, x, y):
        self.reset_visited()
        self.visited[x][y] = 0

        for depth in range(0, 1000):
            visited_one_or_more = False
            for row in range(0, self.num_rows):
                for col in range(0, self.num_cols):
                    if self.visited[row][col] == depth:
                        visited_one_or_more = True
                        if row == self.end_x and col == self.end_y:
                            return self.visited[self.end_x][self.end_y]
                        self.calculate_cell(depth, row, col)
            if not visited_one_or_more:
                return self.visited[self.end_x][self.end_y]

        return self.visited[self.end_x][self.end_y]

    def solve1(self):
        return self.solve_for_start_point(self.start_x, self.start_y)

    def solve2(self):
        """TODO: This implementation is slow! Should refactor to work outwards from the end cell."""
        lowest_score = 100000000
        i = 0
        for row, col in self.start_points_for_part_two:
            i += 1
            score = 0
            score = self.solve_for_start_point(row, col)
            if score != "NO" and score < lowest_score:
                lowest_score = score
        return lowest_score
