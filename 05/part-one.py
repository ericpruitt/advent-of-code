#!/usr/bin/env python3
import sys
import collections

constraints = collections.defaultdict(set)

result = 0

with open(sys.argv[1]) as fd:
    for line in fd:
        if "|" in line:
            left, right = map(int, line.strip().split("|"))
            constraints[left].add(right)
        elif "," in line:
            pages = list(map(int, line.strip().split(",")))

            for index, page in enumerate(pages):
                not_allowed_in_seen = constraints[page]
                seen = set(pages[:index])

                if seen & not_allowed_in_seen:
                    break
            else:
                result += pages[len(pages) // 2]

print(result)
