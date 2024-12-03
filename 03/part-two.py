#!/usr/bin/env python3
import re

INSTRUCTION_RE = re.compile(r"mul[(][0-9]{1,3},[0-9]{1,3}[)]|do\(\)|don't\(\)")

with open("memory") as fd:
    data = fd.read()

result = 0
enabled = True

for instruction in INSTRUCTION_RE.findall(data):
    if instruction == "do()":
        enabled = True
    elif instruction == "don't()":
        enabled = False
    elif enabled:
        arguments = instruction[4:-1]
        left, right = map(int, arguments.split(","))
        result += left * right

print(result)
