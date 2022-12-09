import re
from copy import deepcopy
from os import path
from typing import List, TypedDict

basedir = path.dirname(__file__)
FILE_NAME = path.join(basedir, "input.txt")

extract_instruction_re = re.compile(r"move (?P<quantity>\d+) from (?P<start>\d{1}) to (?P<end>\d{1})")
pile_base = re.compile(r"([1-9]+[ ]+)+")


class Move(TypedDict):
    quantity: str
    start: str
    end: str


def parse_instruction(val: str) -> Move:
    matched = extract_instruction_re.search(val)
    if not matched:
        raise ValueError("No instruction found", val)

    return matched.groupdict()


piles = {}
moves: List[Move] = []
is_parsing_piles = True
waiting_piles = []

with open(FILE_NAME) as f:
    lines = f.readlines()


for line in lines:
    line = line.strip("\n").strip("\r")

    if not line:
        continue

    if is_parsing_piles and pile_base.search(line):
        is_parsing_piles = False
        continue

    if is_parsing_piles:
        objectives = [line[i : i + 4] for i in range(0, len(line), 4)]

        if not piles:
            for i in range(0, len(objectives)):
                piles[str(i+1)] = []

        for i, val in enumerate(objectives):
            val = val.strip().strip("[").strip("]")
            if val:
                piles[str(i+1)].append(val)
    else:
        moves.append(parse_instruction(line))

piles2 = deepcopy(piles)
# Part 1 ---------------------------
for move in moves:
    from_pile = piles[move["start"]]
    to_pile = piles[move["end"]]

    for _ in range(0, int(move["quantity"])):
        to_pile.insert(0, from_pile.pop(0))

print("Answers 1", ''.join(p[0] for p in piles.values()))

# Part 2 ---------------------------
for move in moves:
    from_pile = piles2[move["start"]]
    to_pile = piles2[move["end"]]

    piles2[move["end"]] = from_pile[:int(move["quantity"])] + to_pile
    piles2[move["start"]] = from_pile[int(move["quantity"]):]
        
print("Answers 2", ''.join(p[0] if p else " " for p in piles2.values()))