#!/usr/bin/env python3

from abstractsolver import AbstractSolver


class Solver(AbstractSolver):
    input_lines: list

    def read_input(self, lines: list) -> None:
        self.input_lines = lines

    def solve1(self):
        cubes = []
        for line in self.input_lines:
            ls = line.split(",")
            cubes.append((int(ls[0]), int(ls[1]), int(ls[2])))

        num_cubes = len(cubes)
        num_faces = 6 * num_cubes
        num_faces_hidden = 0

        for i in range(0, num_cubes):
            for j in range(0, num_cubes):
                if i != j:
                    x1, y1, z1 = cubes[i]
                    x2, y2, z2 = cubes[j]
                    if x1 == x2 and y1 == y2 and z1 == z2:
                        print("SAME CUBE ERROR")
                        sys.exit(0)
                    # Compare x,y
                    if x1 == x2 and y1 == y2:
                        if abs(z2 - z1) == 1:
                            num_faces_hidden += 1

                    # Compare y,z
                    if y1 == y2 and z1 == z2:
                        if abs(x2 - x1) == 1:
                            num_faces_hidden += 1

                    # Compare x,z
                    if x1 == x2 and z1 == z2:
                        if abs(y2 - y1) == 1:
                            num_faces_hidden += 1

        num_faces_exposed = num_faces - num_faces_hidden
        return num_faces_exposed

    def solve2(self):
        return -1
