#!/usr/bin/env python3
import sys
import graphlib
import collections

relations = list()
constraints = collections.defaultdict(set)
result = 0

with open(sys.argv[1]) as fd:
    for line in fd:
        if "|" in line:
            left, right = map(int, line.strip().split("|"))
            constraints[left].add(right)
            relations.append((left, right))
        elif "," in line:
            pages = list(map(int, line.strip().split(",")))

            for index, page in enumerate(pages):
                not_allowed_in_seen = constraints[page]
                seen = set(pages[:index])

                if seen & not_allowed_in_seen:
                    break
            else:
                continue

            graph = collections.defaultdict(set)

            for left, right in relations:
                if left not in pages or right not in pages:
                    continue

                graph[right].add(left)

            sorted_pages = list(graphlib.TopologicalSorter(graph).static_order())
            result += sorted_pages[len(sorted_pages) // 2]

print(result)
