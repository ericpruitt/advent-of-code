#!/usr/bin/env python3
import fractions
import collections
import itertools
import re
import sys

F = fractions.Fraction
total = 0
grid = dict()
ants = collections.defaultdict(set)

with open(sys.argv[1]) as fd:
    for y, line in enumerate(fd):
        line = line.strip()
        w = len(line)

        for x, character in enumerate(line):
            if character != ".":
                grid[(x, y)] = character
                ants[character].add((x, y))

h = y + 1
nodes = set()

for points in ants.values():
    for a, b in itertools.combinations(points, 2):
        if a[1] == b[1]:
            y = a[1]

            for x in range(0, w):
                nodes.add((x, y))

        else:
            dx = b[0] - a[0]
            dy = b[1] - a[1]
            slope = F(dy, dx)
            const = b[1] - b[0] * slope

            for x in range(w):
                y = slope * x + const

                if y == int(y) and 0 <= y < h:
                    nodes.add((x, int(y)))

for y in range(h):
    for x in range(w):
        if (x, y) in nodes:
            print("#", end="")
        else:
            print(grid.get((x, y), "."), end="")
    print()

print(len(nodes))
