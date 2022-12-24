#!/usr/bin/env python3

from abstractsolver import AbstractSolver
import json
import sys

ORE = 0
CLAY = 1
OBSIDIAN = 2
GEODE = 3

TYPES = [ORE, CLAY, OBSIDIAN, GEODE]

# To make any robot, need ore, which is plentiful.
#
# From reding the config.
# - ORE robot always costs A ore.
# - CLAY robot always costs B ore.
# - OBSIDIAN robot always costs C ore and D clay.
# - GEODE robot always costs E ore and F obsidian.
#
# So,
# - GEODE robot always costs E ore and F * (C ore and D clay).
# - GEODE robot always costs (E + FC) ore and (FD) clay.
# So, how do I build a single geode robot as fast as possible?
#
class Solver(AbstractSolver):
    blueprints = []
    best_score_for_id = 0
    MAX_TIME = 0  # SET IN SOLVER.

    def read_input(self) -> None:
        for line in self.input_lines:
            line_split = line.split()
            id = int(line_split[1][:-1])
            # self.blueprints.append((id, line_split[6], line_split[12], line_split[18], line_split[21], line_split[27], line_split[30]))
            costs_matrix = [
                [int(line_split[6]), 0, 0],  # ORE robot
                [int(line_split[12]), 0, 0],  # CLAY robot
                [int(line_split[18]), int(line_split[21]), 0],  # OBSIDIAN robot
                [int(line_split[27]), 0, int(line_split[30])],  # GEODE robot
                max(
                    max(int(line_split[6]), int(line_split[12])),
                    max(int(line_split[18]), int(line_split[27])),
                ),  # Max number of ore for anything.
                int(line_split[21]),  # Max number of clay for anything.
                int(line_split[30]),  # Max number of obsidian for geode.
            ]
            self.blueprints.append((id, costs_matrix))

    def key_for(self, num_rc):
        return "{} {} {} {} {} {} {} {}".format(
            num_rc[0],
            num_rc[1],
            num_rc[2],
            num_rc[3],
            num_rc[4],
            num_rc[5],
            num_rc[6],
            num_rc[7],
        )

    def res_key_for(self, num_rc):
        return "{} {} {} {}".format(num_rc[0], num_rc[1], num_rc[2], num_rc[3])

    def robot_key_for(self, num_rc):
        return "{} {} {} {}".format(num_rc[4], num_rc[5], num_rc[6], num_rc[7])

    def expand_paths(self, costs_matrix, pass_idx, current_dict, prev_dict):
        temp_dict = {}
        # Add an extra few to allow it to work.
        time_left_to_spend = self.MAX_TIME - pass_idx + 1 + 5
        max_ore_to_spend = costs_matrix[4] * time_left_to_spend
        max_clay_to_spend = costs_matrix[5] * 5
        # print("DEBUG: time_left_to_spend {}, max_ore {}, max_clay {}".format(time_left_to_spend, max_ore_to_spend, max_clay_to_spend))

        f_out = open("day19-paths-{}.txt".format(pass_idx), "w")
        for rc in current_dict.values():
            # Do nothing.
            # OPTIMISE: If obsidian resources not enough to build a geode, and have enough
            # ore and clay to build all three of the other types, then must build one.
            if rc[ORE] >= costs_matrix[4] and rc[CLAY] >= costs_matrix[5]:
                pass
            elif rc[ORE] >= max_ore_to_spend or rc[CLAY] >= max_clay_to_spend:
                # print(
                #     "DROP: {} because {} {}".format(
                #         rc, max_ore_to_spend, max_clay_to_spend
                #     )
                # )
                pass
            else:
                new_rc = [
                    rc[ORE] + rc[4],
                    rc[CLAY] + rc[5],
                    rc[OBSIDIAN] + rc[6],
                    rc[GEODE] + rc[7],
                    rc[4],
                    rc[5],
                    rc[6],
                    rc[7],
                ]
                new_key = self.key_for(new_rc)
                if new_key in prev_dict:
                    # print("DISCARD-2: {} {}".format(new_key, new_rc))
                    pass
                else:
                    # print("KEEP-2:    {} {}".format(new_key, new_rc))
                    temp_dict[new_key] = new_rc

            for build_type in TYPES:
                costs_matrix_for_type = costs_matrix[build_type]
                # Take care to determine if possible BEFORE adding extra resources.
                if (
                    rc[ORE] >= costs_matrix_for_type[ORE]
                    and rc[CLAY] >= costs_matrix_for_type[CLAY]
                    and rc[OBSIDIAN] >= costs_matrix_for_type[OBSIDIAN]
                ):
                    # Now add the extra resources.
                    inc_4 = 0
                    inc_5 = 0
                    inc_6 = 0
                    inc_7 = 0
                    if build_type == ORE:
                        inc_4 = 1
                    elif build_type == CLAY:
                        inc_5 = 1
                    elif build_type == OBSIDIAN:
                        inc_6 = 1
                    elif build_type == GEODE:
                        inc_7 = 1
                    else:
                        print("ERROR")
                        sys.exit(0)
                    new_rc = [
                        rc[ORE] + rc[4] - costs_matrix_for_type[ORE],
                        rc[CLAY] + rc[5] - costs_matrix_for_type[CLAY],
                        rc[OBSIDIAN] + rc[6] - costs_matrix_for_type[OBSIDIAN],
                        rc[GEODE] + rc[7],
                        rc[4] + inc_4,
                        rc[5] + inc_5,
                        rc[6] + inc_6,
                        rc[7] + inc_7,
                    ]
                    new_key = self.key_for(new_rc)
                    if new_key in prev_dict:
                        # print("DISCARD-1: {} {}".format(new_key, new_rc))
                        pass
                    else:
                        # print("KEEP-1:    {} {}".format(new_key, new_rc))
                        temp_dict[new_key] = new_rc

        # print("COMPARE len_expandable_paths {} with len(temp_dict) {}".format(len_expandable_paths, len(temp_dict)))
        sorted_temp_dict = sorted(temp_dict.items(), key=lambda x: x[1], reverse=True)
        temp_dict = {}
        prev_item = [999, 999, 999, 999, 999, 999, 999, 999]
        max_ore_to_spend -= costs_matrix[4]
        max_clay_to_spend -= costs_matrix[5]

        for data in sorted_temp_dict:
            want_it = True
            item = data[1]
            if (
                item[0] == prev_item[0]
                and item[1] == prev_item[1]
                and item[2] == prev_item[2]
                and item[3] == prev_item[3]
            ):
                if (
                    item[4] <= prev_item[4]
                    and item[5] <= prev_item[5]
                    and item[6] <= prev_item[6]
                    and item[7] <= prev_item[7]
                ):
                    # print("DROP ITEM: {}, prefer {}".format(item, prev_item))
                    want_it = False
            if want_it:
                if item[ORE] >= max_ore_to_spend or item[CLAY] >= max_clay_to_spend:
                    # print("DROP-2: {} because {} {}".format(item, max_ore_to_spend, max_clay_to_spend))
                    want_it = False
            if want_it:
                f_out.write(json.dumps(item) + "\n")
                temp_dict[data[0]] = item
            prev_item = item
        f_out.write("\n")
        f_out.close()
        return temp_dict

    def solve1(self):
        self.MAX_TIME = 24
        best_scores = []
        for id, costs_matrix in self.blueprints:
            # print("PROCESS ID {}".format(id))
            self.best_score_for_id = 0
            first_rc = [0, 0, 0, 0, 1, 0, 0, 0]
            first_key = self.key_for(first_rc)
            current_dict = {}
            current_dict[first_key] = first_rc

            f = open("day19-paths-{}.txt".format(0), "w")
            for key in current_dict:
                f.write(json.dumps(current_dict[key]) + "\n")
            f.write("\n")
            f.close()

            pass_idx = 0
            while len(current_dict) != 0:
                pass_idx += 1
                # print(
                #     "PASS {}, expandable before {}".format(pass_idx, len(current_dict))
                # )

                if pass_idx == (self.MAX_TIME + 1):
                    f_in = open("day19-paths-{}.txt".format(pass_idx - 1))
                    for line in f_in.readlines():
                        if len(line) <= 1:
                            break
                        rc = json.loads(line.rstrip())
                        if rc[GEODE] > self.best_score_for_id:
                            self.best_score_for_id = rc[GEODE]
                        current_dict = {}
                else:
                    prev_dict = current_dict.copy()
                    current_dict = self.expand_paths(
                        costs_matrix, pass_idx, current_dict, prev_dict
                    )

            # print("DONE for ID {}".format(id))

            best_scores.append(
                (id, self.best_score_for_id, id * self.best_score_for_id)
            )
            # print(
            #     "    ID {}, GEODES {}, QUALITY {}".format(
            #         id, self.best_score_for_id, id * self.best_score_for_id
            #     )
            # )

        final_score = 0
        # print("BEST SCORES:")
        for score in best_scores:
            # print(
            #     "    ID {}, GEODES {}, QUALITY {}".format(score[0], score[1], score[2])
            # )
            final_score += score[2]
        return final_score

    def solve2(self):
        self.MAX_TIME = 32
        best_scores = []
        for id, costs_matrix in self.blueprints:
            if id == 4:
                break

            # print("PROCESS ID {}".format(id))
            self.best_score_for_id = 0
            first_rc = [0, 0, 0, 0, 1, 0, 0, 0]
            first_key = self.key_for(first_rc)
            current_dict = {}
            current_dict[first_key] = first_rc

            f = open("day19-paths-{}.txt".format(0), "w")
            for key in current_dict:
                f.write(json.dumps(current_dict[key]) + "\n")
            f.write("\n")
            f.close()

            pass_idx = 0
            while len(current_dict) != 0:
                pass_idx += 1
                # print(
                #     "PASS {}, expandable before {}".format(pass_idx, len(current_dict))
                # )

                if pass_idx == (self.MAX_TIME + 1):
                    f_in = open("day19-paths-{}.txt".format(pass_idx - 1))
                    for line in f_in.readlines():
                        if len(line) <= 1:
                            break
                        rc = json.loads(line.rstrip())
                        if rc[GEODE] > self.best_score_for_id:
                            self.best_score_for_id = rc[GEODE]
                else:
                    prev_dict = current_dict.copy()
                    current_dict = self.expand_paths(
                        costs_matrix, pass_idx, current_dict, prev_dict
                    )

            # print("DONE for ID {}".format(id))

            best_scores.append(
                (id, self.best_score_for_id, id * self.best_score_for_id)
            )
            # print(
            #     "    ID {}, GEODES {}, QUALITY {}".format(
            #         id, self.best_score_for_id, id * self.best_score_for_id
            #     )
            # )

        final_score = 1
        # print("BEST SCORES:")
        for score in best_scores:
            # print(
            #     "    ID {}, GEODES {}, QUALITY {}".format(score[0], score[1], score[2])
            # )
            final_score *= score[1]
        return final_score
