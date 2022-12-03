# file = open('./input.tiny.txt', 'r')
file = open("./input.txt", "r")
lines = file.readlines()

# First challenge
"""
sum = 0
for line in lines:
  half = len(line) // 2
  left_half = line[0:half]
  second_half = line[half: ]

  for letter in left_half:
    if letter in second_half:
      code = ord(letter.upper()) - 64
      sum += code + 26 if letter != letter.lower() else code
      break

print(sum)
"""

# Second challenge
sum = 0
line1 = ''
line2 = ''
line3 = ''

for line in lines:
  # Get lines
  if line1 == '': 
    line1 = line.replace('\n', '')
  elif line2 == "": 
    line2 = line.replace('\n', '')
  elif line3 == "":
    line3 = line.replace('\n', '')

    # Uniques letters 
    uniques = set(line1 + line2 + line3)

    for unique in uniques:
      if unique in line1 and unique in line2 and unique in line3:
        code = ord(unique.upper()) - 64
        sum += code + 26 if unique != unique.lower() else code
        break

    # Clean 
    line1 = line2 = line3 = ""

print(sum)