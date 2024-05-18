import time, sys
import numpy as np
class Rope:
    def __init__(self, length):
        self.length = length
        self.links = []
        self.visited = set()
        self.visited.add((0, 0))

        for i in range(length):
            self.links.append((0, 0))

    def move(self, direction, spaces):
        for i in range(spaces):
            if direction == "L":
                self.links[0] = (self.links[0][0] - 1, self.links[0][1])
            if direction == "R":
                self.links[0] = (self.links[0][0] + 1, self.links[0][1])
            if direction == "U":
                self.links[0] = (self.links[0][0], self.links[0][1] + 1)
            if direction == "D":
                self.links[0] = (self.links[0][0], self.links[0][1] - 1)

            for j in range(1, self.length):
                d_x = self.links[j-1][0] - self.links[j][0]
                d_y = self.links[j-1][1] - self.links[j][1]
                if abs(d_x) > 1 or abs(d_y) > 1:
                    self.links[j] = (self.links[j][0] + np.sign(d_x), self.links[j][1] + np.sign(d_y))
                    if j == self.length - 1:
                        self.visited.add((self.links[j][0], self.links[j][1]))

    def spaces_visited(self):
        return len(self.visited)


rope = Rope(length=2)
for line in [line for line in open("rope_bridge.txt", "r")]:
    instruction = line.split(" ")
    rope.move(instruction[0], int(instruction[-1]))
print(rope.spaces_visited())

rope = Rope(length=10)
for line in [line for line in open("rope_bridge.txt", "r")]:
    instruction = line.split(" ")
    rope.move(instruction[0], int(instruction[-1]))
print(rope.spaces_visited())

