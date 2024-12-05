#!/usr/bin/env python3
import sys

p = lambda x, y: grid[(x, y)]
scans = list()
grid = dict()

with open(sys.argv[1]) as fd:
    for y, line in enumerate(fd):
        line = line.strip().upper()
        w = len(line)

        for x, character in enumerate(line):
            grid[(x, y)] = character

h = y + 1
count = 0

for x in range(1, w - 1):
    for y in range(1, h - 1):
        if p(x, y) != "A":
            continue

        left = p(x - 1, y - 1) + "A" + p(x + 1, y + 1)
        right = p(x - 1, y + 1) + "A" + p(x + 1, y - 1)

        if left in ("MAS", "SAM") and right in ("SAM", "MAS"):
            count += 1

print(count)
