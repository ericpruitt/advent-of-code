#!/usr/bin/env python3
import sys

rotate = {
    "^": ">",
    ">": "V",
    "V": "<",
    "<": "^",
}

m = dict()
def p(x, y): m[(x, y)]
direction = "^"
visited = set()

with open(sys.argv[1]) as fd:
    for y, line in enumerate(fd):
        line = line.strip().upper()
        for x, character in enumerate(line):
            w = len(line)

            if character in ".#":
                m[(x, y)] = character
            else:
                orientation = character
                m[(x, y)] = "."
                guard = (x, y)

    h = y + 1

x, y = guard
while True:
    visited.add((x, y))

    match orientation:
      case "^":
        delta = ( 0, -1)
      case "V":
        delta = ( 0, +1)
      case "<":
        delta = (-1,  0)
      case ">":
        delta = (+1,  0)
      case _:
        1/0

    destination = (x + delta[0], y + delta[1])

    if destination not in m:
        break
    if m[destination] == "#":
        orientation = rotate[orientation]
    else:
        x, y = destination

print(len(visited))
