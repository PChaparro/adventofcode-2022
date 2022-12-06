#file = open('./input.tiny.txt', 'r')
file = open("./input.txt", "r")
#lines = file.readlines()
line = file.readline()

def find_marker(desired_length, buffer):
  for start in range(0, len(buffer) - desired_length - 1):
    end = start + desired_length;

    current_segment = buffer[start:end]
    current_segment = [char for char in current_segment]
    uniques = set(current_segment)
    
    if len(uniques) == desired_length:
      return end

# Toggle these lines to solve challenge 1 or challenge 2
# print(find_marker(4, line))
print(find_marker(14, line))