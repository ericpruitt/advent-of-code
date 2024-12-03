#!/usr/bin/env python3
import re

VALID_MUL_RE = re.compile("mul[(][0-9]{1,3},[0-9]{1,3}[)]")

with open("memory") as fd:
    data = fd.read()

result = 0

for instruction in VALID_MUL_RE.findall(data):
    arguments = instruction[4:-1]
    left, right = map(int, arguments.split(","))
    result += left * right

print(result)
