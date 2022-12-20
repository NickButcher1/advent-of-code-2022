#!/usr/bin/env python3

from abstractsolver import AbstractSolver


class Solver(AbstractSolver):
    inputs = []
    decrypted_inputs = []
    num_inputs: int
    DECRYPTION_KEY = 811589153
    NUM_MIXES = 10

    def read_input(self, input_lines: list) -> None:
        for line in input_lines:
            self.inputs.append(int(line))
            self.decrypted_inputs.append(int(line) * self.DECRYPTION_KEY)
        self.num_inputs = len(self.inputs)

    def solve_common(self, inputs, num_mixes):
        outputs = []
        for idx in range(0, self.num_inputs):
            outputs.append(idx)

        for mix in range(0, num_mixes):
            # Sort the original positions.
            for source_original_pos in range(0, self.num_inputs):
                source_original_value = inputs[source_original_pos]

                for current_pos in range(0, self.num_inputs):
                    if outputs[current_pos] == source_original_pos:
                        break

                target_pos = current_pos + source_original_value
                if target_pos >= self.num_inputs:
                    new_pos = target_pos % (self.num_inputs - 1)
                elif target_pos < 0:
                    new_pos = target_pos % (self.num_inputs - 1)
                else:
                    new_pos = target_pos

                # Move current_pos to target_pos.
                if current_pos > new_pos:
                    while current_pos != new_pos:
                        temp_val = outputs[current_pos]
                        outputs[current_pos] = outputs[current_pos - 1]
                        outputs[current_pos - 1] = temp_val
                        current_pos -= 1
                    if new_pos == 0:
                        # They want you to cycle it to the end.
                        outputs.append(outputs.pop(0))
                elif current_pos < new_pos:
                    while current_pos != new_pos:
                        temp_val = outputs[current_pos]
                        outputs[current_pos] = outputs[current_pos + 1]
                        outputs[current_pos + 1] = temp_val
                        current_pos += 1

            new_positions = []
            for x in outputs:
                new_positions.append(inputs[x])

        # Find position of zero.
        for zero_pos in range(0, self.num_inputs):
            if inputs[outputs[zero_pos]] == 0:
                break

        final_positions = []
        for x in outputs:
            final_positions.append(inputs[x])

        pos_1000 = (1000 + zero_pos) % self.num_inputs
        pos_2000 = (2000 + zero_pos) % self.num_inputs
        pos_3000 = (3000 + zero_pos) % self.num_inputs
        answer_1000 = final_positions[pos_1000]
        answer_2000 = final_positions[pos_2000]
        answer_3000 = final_positions[pos_3000]
        answer_total = answer_1000 + answer_2000 + answer_3000
        return answer_total

    def solve1(self):
        return self.solve_common(self.inputs, 1)

    def solve2(self):
        return self.solve_common(self.decrypted_inputs, 10)
