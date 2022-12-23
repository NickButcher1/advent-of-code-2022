#!/usr/bin/env python3

from abstractsolver import AbstractSolver
import sys

EMPTY = 0
VOID = -1

NORTH = 0
SOUTH = 1
WEST = 2
EAST = 3


class Solver(AbstractSolver):
    input_lines: list
    num_elves: int
    num_rows: int
    num_cols: int
    valid_moves_per_elf: list
    elf_dict: dict  # Lookup from (r,c) tuple to elf ID.
    elf_positions: dict  # Lookup from elf ID to (r,c) tuple.

    def read_input(self, lines: list) -> None:
        self.input_lines = lines

    def reset_solver(self) -> None:
        self.valid_moves_per_elf = [NORTH, SOUTH, WEST, EAST]
        self.elf_dict = {}
        self.elf_positions = {}
        self.num_elves = 0

        self.num_rows = len(self.input_lines)
        self.num_cols = len(self.input_lines[0])

        r = 0
        for line in self.input_lines:
            r += 1

            for i in range(0, self.num_cols):
                if line[i] == "#":
                    self.num_elves += 1
                    self.elf_dict[(r, i + 1)] = self.num_elves
                    self.elf_positions[self.num_elves] = (r, i + 1)

    def caculate_round_1_score(self):
        min_row = 1000000000
        max_row = -1000000000
        min_col = 1000000000
        max_col = -1000000000

        for e in range(1, self.num_elves + 1):
            row, col = self.elf_positions[e]
            if row > max_row:
                max_row = row
            if row < min_row:
                min_row = row
            if col > max_col:
                max_col = col
            if col < min_col:
                min_col = col
        cells = (max_row - min_row + 1) * (max_col - min_col + 1)
        empty_cells = cells

        for e in range(1, self.num_elves + 1):
            row, col = self.elf_positions[e]
            if row >= min_row and row <= max_row and col >= min_col and col <= max_col:
                empty_cells -= 1
        return empty_cells

    def calculate_proposals(self) -> list:
        proposals = {}
        for e in range(1, self.num_elves + 1):
            proposals[e] = None

        for elf_id in range(1, self.num_elves + 1):
            r, c = self.elf_positions[elf_id]
            if (
                (r - 1, c - 1) not in self.elf_dict
                and (r - 1, c) not in self.elf_dict
                and (r - 1, c + 1) not in self.elf_dict
                and (r, c - 1) not in self.elf_dict
                and (r, c + 1) not in self.elf_dict
                and (r + 1, c - 1) not in self.elf_dict
                and (r + 1, c) not in self.elf_dict
                and (r + 1, c + 1) not in self.elf_dict
            ):
                # Elf does not need to move.
                pass
            else:
                found_one = False
                for this_move in self.valid_moves_per_elf:
                    if not found_one:
                        if this_move == NORTH:
                            new_r = r - 1
                            if (
                                (new_r, c - 1) not in self.elf_dict
                                and (new_r, c) not in self.elf_dict
                                and (new_r, c + 1) not in self.elf_dict
                            ):
                                found_one = True
                                proposals[elf_id] = (NORTH, new_r, c)
                        elif this_move == SOUTH:
                            new_r = r + 1
                            if (
                                (new_r, c - 1) not in self.elf_dict
                                and (new_r, c) not in self.elf_dict
                                and (new_r, c + 1) not in self.elf_dict
                            ):
                                found_one = True
                                proposals[elf_id] = (SOUTH, new_r, c)
                        elif this_move == WEST:
                            new_c = c - 1
                            if (
                                (r - 1, new_c) not in self.elf_dict
                                and (r, new_c) not in self.elf_dict
                                and (r + 1, new_c) not in self.elf_dict
                            ):
                                found_one = True
                                proposals[elf_id] = (WEST, r, new_c)
                        elif this_move == EAST:
                            new_c = c + 1
                            if (
                                (r - 1, new_c) not in self.elf_dict
                                and (r, new_c) not in self.elf_dict
                                and (r + 1, new_c) not in self.elf_dict
                            ):
                                found_one = True
                                proposals[elf_id] = (EAST, r, new_c)
                        else:
                            print("ERROR")
                            sys.exit()

        self.valid_moves_per_elf.append(self.valid_moves_per_elf.pop(0))

        return proposals

    def solve_common(self) -> int:
        self.reset_solver()

        for round in range(1, 1000):
            proposals = self.calculate_proposals()
            targets = {}
            for e in range(1, self.num_elves + 1):
                if proposals[e] != None:
                    this_move, new_r, new_c = proposals[e]
                    old_pos = self.elf_positions[e]
                    new_pos = (new_r, new_c)

                    if not new_pos in targets:
                        targets[new_pos] = []
                    targets[new_pos].append(e)

            if self.is_part_two and len(targets) == 0:
                return round

            for key in targets.keys():
                elves = targets[key]
                if len(elves) == 1:
                    elf_id = elves[0]
                    old_pos = self.elf_positions[elf_id]
                    new_pos = key
                    del self.elf_dict[old_pos]
                    if new_pos in self.elf_dict:
                        print("ERROR")
                        sys.exit(0)
                    self.elf_dict[new_pos] = elf_id
                    self.elf_positions[elf_id] = (new_pos[0], new_pos[1])

            if not self.is_part_two and round == 10:
                return self.caculate_round_1_score()

    def solve1(self):
        return self.solve_common()

    def solve2(self):
        return self.solve_common()
