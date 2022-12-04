#file = open('./input.tiny.txt', 'r')
file = open("./input.txt", "r")
lines = file.readlines()

counter = 0

"""
# PART 1
for line in lines:
    line = line.replace("\n", "")

    [elf1, elf2] = line.split(",")
    [elf1_start, elf1_end] = elf1.split("-")
    [elf2_start, elf2_end] = elf2.split("-")
    
    first_contains_second = int(elf1_start) <= int(elf2_start) and int(elf1_end) >= int(
        elf2_end
    )
    
    second_contains_first = int(elf2_start) <= int(elf1_start) and int(elf2_end) >= int(
        elf1_end
    )

    if first_contains_second or second_contains_first:
        counter += 1

print(counter)
"""

# Part 2
for line in lines:
    line = line.replace("\n", "")

    [elf1, elf2] = line.split(",")
    [elf1_start, elf1_end] = elf1.split("-")
    [elf2_start, elf2_end] = elf2.split("-")

    range1 = [x for x in range (int(elf1_start), int(elf1_end) + 1)]
    range1_overlap = False
    range2 = [x for x in range (int(elf2_start), int(elf2_end) + 1)]
    
    # Not really proud of this solution (TODO: Optimize this)
    for x in range1:
      if x in range2:
        counter += 1
        range1_overlap = True
        break

    # Not really proud of this solution (TODO: Optimize this)
    if not range1_overlap:
      for x in range2:
        if x in range1:
          counter += 1
          break


print(counter)