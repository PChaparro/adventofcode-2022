# file = open("./input.tiny.txt", "r")
file = open("./input.txt", "r")
lines = file.readlines()

stack = []
sizes = {}

for line in lines:
    line = line.replace("\n", "")

    if line == "$ cd /":
        # print("Clearing all")
        stack = ["/"]
    elif line == "$ cd ..":
        # print("Going back")
        stack.pop()
    elif line == "$ ls":
        continue
    elif line.startswith("$ cd"):
        # print("Going to a folder")
        [dollar, cd, folder] = line.split(" ")

        path = stack[-1]
        path += "/{}".format(folder) if path != "/" else folder
        stack.append(path)
    else:
        # File or directory
        [size, name] = line.split(" ")

        # Ignore directories
        if size == "dir":
            # print("Ignoring folder")
            continue

        # Add the size to each folder in the current path
        for folder in stack:
            if folder not in sizes.keys():
                sizes[folder] = int(size)
            else:
                sizes[folder] += int(size)

"""
for path in sizes:
  print(path, sizes[path])
"""

"""
# Part 1
acc = 0

for folder in sizes.keys():
  if sizes[folder] <= 100000:
    acc += sizes[folder]

print(acc)
"""

# Part 2
total_size = 70_000_000
update_size = 30_000_000
used_size = sizes["/"]
needed_size = abs(total_size - used_size - update_size)

min_size = total_size

for key in sizes.keys():
    if sizes[key] >= needed_size:
        min_size = min(sizes[key], min_size)

print(min_size)
