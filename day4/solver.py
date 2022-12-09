from os import path
from typing import List

basedir = path.dirname(__file__)
FILE_NAME = path.join(basedir, "input.txt")


def str_range_to_list(val: str) -> List[int]:
    low, high = val.split("-")
    return list(range(int(low), int(high) + 1))


def fully_contained(a: List[int], b: List[int]) -> bool:
    sa = set(a)
    sb = set(b)
    return sa.issubset(sb) or sa.issuperset(sb)


def overlap(a: List[int], b: List[int]) -> bool:
    for room in a:
        if room in b:
            return True

    return False


# Part 1 ---------------------------
with open(FILE_NAME) as f:
    lines = f.readlines()


nb_full_contained_pairs = 0
nb_overlap = 0
for line in lines:
    line = line.strip("\n").strip("\r")
    c1, c2 = line.split(",")

    assign1, assign2 = str_range_to_list(c1), str_range_to_list(c2)

    if overlap(assign1, assign2):
        nb_overlap += 1

        if fully_contained(assign1, assign2):
            nb_full_contained_pairs += 1

print("Answers", nb_full_contained_pairs, nb_overlap)
