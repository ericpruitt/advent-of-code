#!/usr/bin/env python3
def sign(x):
    if x < 0:
        return -1

    return 1


safe = 0

with open("reports") as fd:
    for line in fd:
        values = [int(x) for x in line.split()]

        if values[0] != values[1]:
            direction = sign(values[1] - values[0])
            previous = values[0]

            for value in values[1:]:
                delta = value - previous

                if sign(delta) != direction:
                    break

                if delta not in (-1, -2, -3, 1, 2, 3):
                    break

                previous = value
            else:
                safe += 1

print(safe)
