#!/usr/bin/env python3
import collections

a = []
b = []

b_counts = collections.defaultdict(int)

with open("lists") as fd:
    for line in fd:
        left, right = map(int, line.split())
        a.append(left)
        b_counts[right] += 1

result = 0

for value in a:
    result += value * b_counts[value]

print(result)
