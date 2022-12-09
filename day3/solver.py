from os import path

basedir = path.dirname(__file__)
FILE_NAME = path.join(basedir, "input.txt")


def char_to_int(val: str) -> int:
    if val.islower():
        return ord(val) - ord("a") + 1

    return ord(val) - (ord("A")) + 27


# Part 1 ---------------------------
with open(FILE_NAME) as f:
    lines = f.readlines()


missplaced_items = []
for line in lines:
    line = line.strip("\n").strip("\r")
    c1, c2 = line[: len(line) // 2], line[len(line) // 2 :]

    missplaced_items.extend(set([c for c in c1 if c in c2]))

print("Answers p1", sum([char_to_int(i) for i in missplaced_items]))

# Part2
badge_per_group = []
for group in [lines[i : i + 3] for i in range(0, len(lines), 3)]:
    elf1, elf2, elf3 = (
        group[0].strip("\n").strip("\r"),
        group[1].strip("\n").strip("\r"),
        group[2].strip("\n").strip("\r"),
    )

    badge_per_group.extend(set([c for c in elf1 if c in elf2 and c in elf3]))

print("Answers p1", sum([char_to_int(i) for i in badge_per_group]))
