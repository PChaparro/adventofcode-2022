#file = open("./input.tiny.txt", "r")
file = open("./input.txt", "r")
lines = file.readlines()

grid = []
visibles_count = 0
max_score = 0

# Receive
for line in lines:
    line = line.replace("\n", "")
    grid.append([height for height in line])

# Count (Ignoring the edges)
for row_index in range(1, len(grid) - 1):
    for col_index in range(1, len(grid[0]) - 1):
        current_tree = grid[row_index][col_index]
        current_check_row = row_index - 1
        current_check_col = col_index + 1

        taller_top = [0, col_index]
        taller_bottom = [len(grid) - 1, col_index]
        taller_right = [row_index, len(grid[0]) - 1]
        taller_left = [row_index, 0]

        is_visible_top = True
        is_visible_right = True
        is_visible_bottom = True
        is_visible_left = True

        # Check top
        while current_check_row >= 0:
            if grid[current_check_row][col_index] >= current_tree:
                taller_top = [current_check_row, col_index]
                is_visible_top = False
                break

            current_check_row -= 1

        # Check bottom
        current_check_row = row_index + 1
        while current_check_row < len(grid):
            if grid[current_check_row][col_index] >= current_tree:
                taller_bottom = [current_check_row, col_index]
                is_visible_bottom = False
                break

            current_check_row += 1

        # Check right
        while current_check_col < len(grid[0]):
            if grid[row_index][current_check_col] >= current_tree:
                taller_right = [row_index, current_check_col]
                is_visible_right = False
                break

            current_check_col += 1

        # Check left
        current_check_col = col_index - 1
        while current_check_col >= 0:
            if grid[row_index][current_check_col] >= current_tree:
                taller_left = [row_index, current_check_col]
                is_visible_left = False
                break

            current_check_col -= 1

        # print('[{}][{}]'.format(row_index, col_index), is_visible_top, is_visible_right, is_visible_bottom, is_visible_left)
        if is_visible_top or is_visible_bottom or is_visible_left or is_visible_right:
            visibles_count += 1

        # Calc the new max score
        current_score = (
            abs(taller_top[0] - row_index)
            * abs(taller_right[1] - col_index)
            * abs(taller_bottom[0] - row_index)
            * abs(taller_left[1] - col_index)
        )

        max_score = max(max_score, current_score)
        # print(taller_top, taller_right, taller_bottom, taller_left)

block_edge = len(grid[0])
inline_edge = len(grid) - 2  # Substrack the block edge

print("Visibles", visibles_count + block_edge * 2 + inline_edge * 2) # Part 1
print("Score:", max_score) # Part 2
