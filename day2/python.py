file = open("./input.txt", "r")
lines = file.readlines()

values = {"X": 1, "Y": 2, "Z": 3}

# A rock B paper C Scissors
# X rock Y Paper Z Scissors
patterm = {"A": ["Y", "X", "Z"], "B": ["Z", "Y", "X"], "C": ["X", "Z", "Y"]}

score = 0

for line in lines:
    elf = line[0]
    expected = line[2]
    player = ""

    if expected == "X":
        # Loose
        player = patterm[elf][2]
    elif expected == "Y":
        # Tie
        player = patterm[elf][1]
        score += 3
    else:
        # Won
        player = patterm[elf][0]
        score += 6

    score += values[player]

print(score)
