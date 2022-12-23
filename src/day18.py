#!/usr/bin/env python3

from abstractsolver import AbstractSolver
import numpy


class Solver(AbstractSolver):
    def read_input(self) -> None:
        pass

    def count_air(self):
        air_count = 0
        for x in range(1, maxes[0] - 1):
            for y in range(1, maxes[1] - 1):
                for z in range(1, maxes[2] - 1):
                    if matrix[x][y][z] == 0:
                        air_count += 1
        return air_count

    # Now work inwards.
    def parse_matrix(self, matrix, maxes):
        fill_count = 0
        for x in range(1, maxes[0] - 1):
            for y in range(1, maxes[1] - 1):
                for z in range(1, maxes[2] - 1):
                    # Look at air that is touching the external edges. Can we turn it into an external edge?
                    # We are guaranteed that there is already an "external edge" cube towards the edge in
                    # every direction, so don't have to worry about array indexing.
                    if matrix[x][y][z] == 0:
                        touching_external = 0
                        if matrix[x + 1][y][z] == 2:
                            touching_external += 1
                        elif matrix[x - 1][y][z] == 2:
                            touching_external += 1
                        elif matrix[x][y + 1][z] == 2:
                            touching_external += 1
                        elif matrix[x][y - 1][z] == 2:
                            touching_external += 1
                        elif matrix[x][y][z + 1] == 2:
                            touching_external += 1
                        elif matrix[x][y][z - 1] == 2:
                            touching_external += 1
                        else:
                            pass
                        if touching_external != 0:
                            matrix[x][y][z] = 2
                            fill_count += 1
                    elif matrix[x][y][z] == 1:
                        pass  # print("IGNORE FILLED CELL {},{},{}".format(x,y,z))
                    else:
                        pass  # print("IGNORE EXTERNAL EDGE {},{},{}".format(x,y,z))
        return fill_count

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
        maxes = [0, 0, 0]

        cubes = []
        for line in self.input_lines:
            ls = line.split(",")
            cube = (1 + int(ls[0]), 1 + int(ls[1]), 1 + int(ls[2]))
            cubes.append(cube)
            if cube[0] > maxes[0]:
                maxes[0] = cube[0]
            if cube[1] > maxes[1]:
                maxes[1] = cube[1]
            if cube[2] > maxes[2]:
                maxes[2] = cube[2]

        num_cubes = len(cubes)
        num_faces = 6 * num_cubes
        num_faces_hidden = 0
        maxes[0] += 3
        maxes[1] += 3
        maxes[2] += 3
        matrix = numpy.zeros((maxes[0], maxes[1], maxes[2]))

        # Fill in the external edges.
        for x in range(0, maxes[0]):
            for y in range(0, maxes[1]):
                for z in range(0, maxes[2]):
                    if x == 0 or x == (maxes[0] - 1):
                        matrix[x][y][z] = 2
                    elif y == 0 or y == (maxes[1] - 1):
                        matrix[x][y][z] = 2
                    elif z == 0 or z == (maxes[2] - 1):
                        matrix[x][y][z] = 2

        # Fill the matrix.
        # 0 = unknown
        # 1 = cube
        # 2 = external
        for i in range(0, num_cubes):
            x, y, z = cubes[i]
            matrix[x][y][z] = 1

        # Fill in all external edges.
        fill_count = -1
        while fill_count != 0:
            fill_count = self.parse_matrix(matrix, maxes)

        exposed_to_external_count = 0
        cube_check = 0

        for x in range(1, maxes[0] - 1):
            for y in range(1, maxes[1] - 1):
                for z in range(1, maxes[2] - 1):
                    if matrix[x][y][z] == 1:
                        # This is a cube.  Now identify whether the six adjacent cells are external edges.
                        cube_check += 1
                        touching_external = 0
                        if matrix[x + 1][y][z] == 2:
                            touching_external += 1
                        if matrix[x - 1][y][z] == 2:
                            touching_external += 1
                        if matrix[x][y + 1][z] == 2:
                            touching_external += 1
                        if matrix[x][y - 1][z] == 2:
                            touching_external += 1
                        if matrix[x][y][z + 1] == 2:
                            touching_external += 1
                        if matrix[x][y][z - 1] == 2:
                            touching_external += 1

                        if touching_external != 0:
                            exposed_to_external_count += touching_external

        return exposed_to_external_count
