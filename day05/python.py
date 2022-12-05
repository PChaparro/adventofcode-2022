# file = open("./input.tiny.txt", "r")
file = open("./input.txt", "r")
lines = file.readlines()

# crates = [["Z", "N"], ["M", "C", "D"], ["P"]]

crates = [
    ["N", "S", "D", "C", "V", "Q", "T"],
    ["M", "F", "V"],
    ["F", "Q", "W", "D", "P", "N", "H", "M"],
    ["D", "Q", "R", "T", "F"],
    ["R", "F", "M", "N", "Q", "H", "V", "B"],
    ["C", "F", "G", "N", "P", "W", "Q"],
    ["W", "F", "R", "L", "C", "T"],
    ["T", "Z", "N", "S"],
    ["M", "S", "D", "J", "R", "Q", "H", "N"],
]

# Part one
for line in lines:
    line = line.replace("\n", "")
    words = line.split(" ")
    amount = int(words[1])
    from_col = int(words[3])
    to_col = int(words[5])

    # Save in auxiliar array
    movement = crates[from_col - 1][-amount:]

    # Uncomment this line to solve part 1
    # Comment this line to solve part 2
    # movement.reverse()

    # Remove from current column
    crates[from_col - 1] = crates[from_col - 1][: len(crates[from_col - 1]) - amount]

    # Append to the final column
    crates[to_col - 1] = crates[to_col - 1] + movement

final_rearrangement = ""

for crate in crates:
    if len(crate) != 0:
        final_rearrangement += crate[len(crate) - 1]

print(final_rearrangement)
