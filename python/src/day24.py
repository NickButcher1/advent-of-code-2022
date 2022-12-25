#!/usr/bin/env python3

from abstractsolver import AbstractSolver
import sys


class Solver(AbstractSolver):
    num_rows: int
    num_cols: int
    matrix: list
    matrix_per_minute: list
    start_pos: tuple
    target_pos: tuple
    solved_part_a = False
    solved_part_b = False
    solved_part_c = False

    def read_input(self) -> None:
        pass

    def print_matrix(self, matrix):
        for i in range(0, self.num_rows):
            output = ""
            for j in range(0, self.num_cols):
                cell = matrix[i][j]
                if len(cell) == 0:
                    output += "."
                elif len(cell) == 1:
                    output += cell[0]
                else:
                    output += str(len(cell))
            print(output)

    def reset_data(self) -> None:
        self.num_rows = len(self.input_lines)
        self.num_cols = len(self.input_lines[0])
        self.start_pos = (0, len(self.input_lines[0].split(".")[0]))
        self.target_pos = (
            len(self.input_lines) - 1,
            len(self.input_lines[len(self.input_lines) - 1].split(".")[0]),
        )
        self.matrix = []
        for row_idx in range(0, self.num_rows):
            row = []
            self.matrix.append(row)
            for col_idx in range(0, self.num_cols):
                cell_list = []
                content = self.input_lines[row_idx][col_idx]
                if content in ["<", ">", "^", "v"]:
                    row.append([self.input_lines[row_idx][col_idx]])
                elif content == ".":
                    row.append([])
                else:
                    row.append([content])

        self.matrix[self.start_pos[0]][self.start_pos[1]] = "S"
        self.matrix[self.target_pos[0]][self.target_pos[1]] = "E"

        self.matrix_per_minute = []
        self.matrix_per_minute.append(self.matrix)

    def flow_one_step(self):
        new_matrix = []

        for i in range(0, self.num_rows):
            new_row = []
            new_matrix.append(new_row)
            for j in range(0, self.num_cols):
                new_row.append([])

        for i in range(0, self.num_rows):
            new_row = []
            new_matrix.append(new_row)
            for j in range(0, self.num_cols):
                for cell_content in self.matrix[i][j]:
                    if cell_content == "<":
                        new_j = j - 1
                        if new_j == 0:
                            new_j = self.num_cols - 2
                        new_matrix[i][new_j].append("<")
                    elif cell_content == ">":
                        new_j = j + 1
                        if new_j == (self.num_cols - 1):
                            new_j = 1
                        new_matrix[i][new_j].append(">")
                    elif cell_content == "^":
                        new_i = i - 1
                        if new_i == 0:
                            new_i = self.num_rows - 2
                        new_matrix[new_i][j].append("^")
                    elif cell_content == "v":
                        new_i = i + 1
                        if new_i == (self.num_rows - 1):
                            new_i = 1
                        new_matrix[new_i][j].append("v")
                    else:
                        new_matrix[i][j].append(cell_content)

        self.matrix = new_matrix
        self.matrix_per_minute.append(self.matrix)

    def is_valid_move(self, matrix, i, j):
        if i == -1:
            return False
        elif i == (self.num_rows):
            return False
        elif matrix[i][j] == ["E"] and (
            not self.solved_part_b or not self.solved_part_c
        ):
            return True
        elif matrix[i][j] == ["S"] and self.solved_part_a and not self.solved_part_b:
            return True
        elif i == 0 or j == 0:
            return False
        elif i == (self.num_rows - 1) or j == (self.num_cols - 1):
            return False
        elif matrix[i][j] == []:
            return True
        else:
            return False

    def get_valid_moves(self, matrix, human_pos) -> list:
        valid_moves = []

        if self.is_valid_move(matrix, human_pos[0] - 1, human_pos[1]):
            valid_moves.append((human_pos[0] - 1, human_pos[1]))
        if self.is_valid_move(matrix, human_pos[0] + 1, human_pos[1]):
            valid_moves.append((human_pos[0] + 1, human_pos[1]))
        if self.is_valid_move(matrix, human_pos[0], human_pos[1] - 1):
            valid_moves.append((human_pos[0], human_pos[1] - 1))
        if self.is_valid_move(matrix, human_pos[0], human_pos[1] + 1):
            valid_moves.append((human_pos[0], human_pos[1] + 1))
        # Wait in place.
        if self.is_valid_move(matrix, human_pos[0], human_pos[1]):
            valid_moves.append((human_pos[0], human_pos[1]))
        elif human_pos[0] == 0 and human_pos[1] == 1:
            valid_moves.append((human_pos[0], human_pos[1]))

        return valid_moves

    def solve_for_depth(self, matrix, depth, human_pos):
        valid_moves = self.get_valid_moves(matrix, human_pos)
        return valid_moves

    def solve_common(self):
        self.reset_data()
        target_pos = self.target_pos

        depth = 1
        self.flow_one_step()
        matrix = self.matrix_per_minute[depth]
        valid_moves = self.solve_for_depth(matrix, depth, self.start_pos)

        while True:
            depth += 1
            self.flow_one_step()
            matrix = self.matrix_per_minute[depth]
            new_valid_moves = []
            for move in valid_moves:
                new_valid_moves += self.solve_for_depth(matrix, depth, move)
            # Remove duplicates.
            valid_moves = list(dict.fromkeys(new_valid_moves))

            if target_pos in valid_moves:
                if not self.is_part_two:
                    return depth
                elif not self.solved_part_a:
                    self.solved_part_a = True
                    valid_moves = [target_pos]
                    target_pos = self.start_pos
                elif not self.solved_part_b:
                    self.solved_part_b = True
                    valid_moves = [target_pos]
                    target_pos = self.target_pos
                elif not self.solved_part_c:
                    self.solved_part_c = True
                    return depth

    def solve1(self):
        return self.solve_common()

    def solve2(self):
        return self.solve_common()
