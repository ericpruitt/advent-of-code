#!/usr/bin/env python3
import sys

scans = list()
grid = dict()

with open(sys.argv[1]) as fd:
    for y, line in enumerate(fd):
        line = line.strip().upper()
        w = len(line)

        for x, character in enumerate(line):
            grid[(x, y)] = character

h = y + 1

edges = []

for x in range(w):
    y = 0
    edges.append((x, y))

for y in range(1, h):
    edges.append((0, y))

for x, y in edges:
    scan = ""

    while True:
        p = (x, y)

        if p not in grid:
            break

        scan += grid[p]

        x += 1
        y += 1

    scans.append(scan)

edges = []

for x in range(w):
    y = h - 1
    edges.append((x, y))

for y in range(1, h - 1):
    edges.append((0, y))

for x, y in edges:
    scan = ""

    while True:
        p = (x, y)

        if p not in grid:
            break

        scan += grid[p]

        x += 1
        y -= 1

    scans.append(scan)

for x in range(w):
    y = 0
    scan = ""

    while True:
        p = (x, y)

        if p not in grid:
            break

        scan += grid[p]

        y += 1

    scans.append(scan)

for y in range(h):
    x = 0
    scan = ""

    while True:
        p = (x, y)

        if p not in grid:
            break

        scan += grid[p]

        x += 1

    scans.append(scan)

count = 0

for scan in scans:
    count += scan.upper().count("XMAS")
    count += scan.upper().count("SAMX")

print(count)
