from enum import Enum
from os import path

basedir = path.dirname(__file__)
FILE_NAME = path.join(basedir, "input.txt")


class Play(str, Enum):
    ROCK = "rock"
    PAPER = "paper"
    SCISSORS = "scissors"


class Results(str, Enum):
    VICTORY = "victory"
    DEFEAT = "defeat"
    DRAW = "draw"


points = {
    Play.ROCK: 1,
    Play.PAPER: 2,
    Play.SCISSORS: 3,
    Results.VICTORY: 6,
    Results.DEFEAT: 0,
    Results.DRAW: 3
}

with open(FILE_NAME) as f:
    lines = f.readlines()

# Part 1 ---------------------------
rounds = []
for line in lines:
    enemy, player = line.strip("\n").split(" ")

    match enemy:
        case "A":
            enemy_play = Play.ROCK
        case "B":
            enemy_play = Play.PAPER
        case "C":
            enemy_play = Play.SCISSORS
        case _:
            raise ValueError("Unexpected token", enemy)

    match player:
        case "X":
            player_play = Play.ROCK
        case "Y":
            player_play = Play.PAPER
        case "Z":
            player_play = Play.SCISSORS
        case _:
            raise ValueError("Unexpected token", player)

    match (enemy_play, player_play):
        case (Play.ROCK, Play.SCISSORS) | (Play.SCISSORS, Play.PAPER) | (Play.PAPER, Play.ROCK):
            result = Results.DEFEAT
            enemy_result = Results.VICTORY
        case (Play.ROCK, Play.ROCK) | (Play.SCISSORS, Play.SCISSORS) | (Play.PAPER, Play.PAPER):
            result = Results.DRAW
            enemy_result = Results.DRAW
        case _:
            result = Results.VICTORY
            enemy_result = Results.DEFEAT

    rounds.append((points[player_play] + points[result], points[enemy_play]+points[enemy_result]))

print("Answers p1", sum([r[0] for r in rounds]))

# Part2
rounds_m2 = []
for line in lines:
    enemy, expected_result = line.strip("\n").split(" ")

    match enemy:
        case "A":
            enemy_play = Play.ROCK
        case "B":
            enemy_play = Play.PAPER
        case "C":
            enemy_play = Play.SCISSORS
        case _:
            raise ValueError("Unexpected token", enemy)

    match expected_result:
        case "X":
            result = Results.DEFEAT
        case "Y":
            result = Results.DRAW
        case "Z":
            result = Results.VICTORY
        case _:
            raise ValueError("Unexpected token", expected_result)

    match enemy_play:
        case Play.ROCK:
            match result:
                case Results.VICTORY:
                    player_play = Play.PAPER
                case Results.DEFEAT:
                    player_play = Play.SCISSORS
                case _:
                    player_play = Play.ROCK
        case Play.SCISSORS:
            match result:
                case Results.VICTORY:
                    player_play = Play.ROCK
                case Results.DEFEAT:
                    player_play = Play.PAPER
                case _:
                    player_play = Play.SCISSORS
        case Play.PAPER:
            match result:
                case Results.VICTORY:
                    player_play = Play.SCISSORS
                case Results.DEFEAT:
                    player_play = Play.ROCK
                case _:
                    player_play = Play.PAPER
                    
    rounds_m2.append(points[player_play] + points[result])
    
print("Answers p2", sum([r for r in rounds_m2]))
