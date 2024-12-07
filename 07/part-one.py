#!/usr/bin/env python3
import itertools
import re
import sys

ops = ["+", "*"]

total = 0

with open(sys.argv[1]) as fd:
    for line in fd:
        line = line.strip()
        left, right = line.split(":")
        target = int(left)
        values = list(map(int, right.split()))

        gaps = len(values) - 1
        options = [list(ops) for _ in range(gaps)]

        for combo in itertools.product(*options):
            result = values[0]

            for op, k in enumerate(range(1, len(values))):
                if combo[op] == "*":
                    result *= values[k]
                elif combo[op] == "+":
                    result += values[k]

            if result == target:
                total += result
                print("possible", line, combo)
                break
        else:
            print("impossible", line)

print(total)
