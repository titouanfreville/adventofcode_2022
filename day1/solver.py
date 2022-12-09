from os import path

basedir = path.dirname(__file__)
FILE_NAME = path.join(basedir, "input.txt")


with open(FILE_NAME) as f:
    data = f.read()

    lines = data.replace("\r", "").split("\n\n")

elves_carries = [
    sum([int(a) for a in line.split("\n") if a]) for line in lines
]

elves_carries.sort(reverse=True)

print("Answers ", elves_carries[0], sum(elves_carries[:3]))