import operator
from functools import reduce
from pathlib import Path

data = Path(__file__).with_suffix(".txt").read_text()

max_colors = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

total = 0

for i, line in enumerate(data.splitlines(), start=1):
    rounds = line.split(": ")[1].split("; ")
    rounds = [x.split(", ") for x in rounds]

    game_possible = True

    for groups in rounds:
        for group in groups:
            count, name = group.split()

            if int(count) > max_colors[name]:
                game_possible = False

    if game_possible:
        total += i

print(total)

total = 0

for i, line in enumerate(data.splitlines(), start=1):
    rounds = line.split(": ")[1].split("; ")
    rounds = [x.split(", ") for x in rounds]

    maxes = {"red": 0, "green": 0, "blue": 0}

    for groups in rounds:
        for group in groups:
            count, name = group.split()

            maxes[name] = max(int(count), maxes[name])

    total += reduce(operator.mul, maxes.values())

print(total)
