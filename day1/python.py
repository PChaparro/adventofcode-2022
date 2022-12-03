file = open('./input.txt', 'r')
lines = file.readlines()

values = []
curr = 0

for line in lines: 
  clean = line.strip()

  if clean == '':
    values.append(curr)
    curr = 0
    continue

  curr += int(clean)

values.sort()
print(values)
print(sum(values[-3:]))
