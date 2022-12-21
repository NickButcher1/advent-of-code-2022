#!/usr/bin/env python3

from abstractsolver import AbstractSolver

class Sensor():
    def __init__(self, x, y, beacon_x, beacon_y):
        self.x = x
        self.y = y
        self.beacon_x = beacon_x
        self.beacon_y = beacon_y
        self.manhat = "UNSET"

    def display(self):
        print("SENSOR: {},{}, beacon {},{}  manhat = {}".format(self.x, self.y, self.beacon_x, self.beacon_y, self.manhat))

class Solver(AbstractSolver):
    input_lines: list
    sensors = []
    min_x = 10000
    max_x = -10000
    TEST_ROW = 2000000

    def read_input(self, lines: list) -> None:
        for line in lines:
            line = line.split()
            self.sensors.append(Sensor(
                int(line[2].split("=")[1][:-1]),
                int(line[3].split("=")[1][:-1]),
                int(line[8].split("=")[1][:-1]),
                int(line[9].split("=")[1])
            ))

        for sensor in self.sensors:
            # There can be no beacon within sensor.manhat distance inclusive.
            sensor.manhat = abs(sensor.x - sensor.beacon_x) + abs(sensor.y - sensor.beacon_y)
            if sensor.x < self.min_x:
                min_x = sensor.x
            if sensor.x > self.max_x:
                self.max_x = sensor.x

        # TODO: Hardcoded.
        self.min_x = -1250000
        self.max_x = 5000000
        print("min_x {}, max_x {}".format(self.min_x, self.max_x))

    def calculate_output(self, row) -> int:
        output = ""
        for char in row:
            output += char
        count_hash = output.count("#")
        count_beacon = output.count("B")
        print(output + "    " + str(count_hash) + " " + str(count_beacon) + " " + str(count_hash + count_beacon))
        return count_hash

    def solve1(self):
        # Initialise the row.
        the_row = []
        for x in range(self.min_x, self.max_x + 1):
            the_row.append(".")

        # Add beacons to the row.
        for sensor in self.sensors:
            if sensor.beacon_y == self.TEST_ROW:
                the_row[sensor.beacon_x - self.min_x] = "B"

        # BUG IS HERE
        # SENSOR: 0,11, beacon 2,10  manhat = 2
        # .........###.............................    3 0 3

        for sensor in self.sensors:
            sensor.display()

            # the_row = []
            # for x in range(min_x, max_x + 1):
            #     the_row.append(".")

            for x in range(self.min_x, self.max_x + 1):
                manhat_to_x_y = abs(sensor.x - x) + abs(sensor.y - self.TEST_ROW)
                if manhat_to_x_y <= sensor.manhat:
                    # X,Y cannot contain a beacon.
                    if the_row[x - self.min_x] != "B":
                        the_row[x - self.min_x] = "#"

        return self.calculate_output(the_row)

    def solve2(self):
        return -1
