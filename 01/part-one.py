#!/usr/bin/env python3

a = []
b = []

with open("lists") as fd:
    for line in fd:
        left, right = map(int, line.split())
        a.append(left)
        b.append(right)

result = 0

for left, right in zip(sorted(a), sorted(b)):
    delta = abs(left - right)
    result += delta

print(result)
