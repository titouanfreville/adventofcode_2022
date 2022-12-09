import re
from copy import deepcopy
from os import path
from typing import List, TypedDict

basedir = path.dirname(__file__)
FILE_NAME = path.join(basedir, "input.txt")

pos = 4
buff = []

# Part 1
with open(FILE_NAME) as f:
    buff = list(f.read(4))
    next_val = ""

    while len(buff) != len(set(buff)) and next_val is not None:
        t = list(set(buff))
        pos += 1
        buff.pop(0)
        next_val = f.read(1)
        buff.append(next_val)


print(pos)

# Part 2

pos = 14
buff = []
with open(FILE_NAME) as f:
    buff = list(f.read(14))
    next_val = ""

    while len(buff) != len(set(buff)) and next_val is not None:
        t = list(set(buff))
        pos += 1
        buff.pop(0)
        next_val = f.read(1)
        buff.append(next_val)


print(pos)