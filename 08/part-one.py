#!/usr/bin/env python3
import collections
import itertools
import re
import sys

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
        dx = b[0] - a[0]
        dy = b[1] - a[1]

        jx = a[0] - dx
        jy = a[1] - dy

        if 0 <= jx < w and 0 <= jy < h:
            nodes.add((jx, jy))

        kx = b[0] + dx
        ky = b[1] + dy

        if 0 <= kx < w and 0 <= ky < h:
            nodes.add((kx, ky))

for y in range(h):
    for x in range(w):
        if (x, y) in nodes:
            print("#", end="")
        else:
            print(grid.get((x, y), "."), end="")
    print()

print(len(nodes))
