f = open("day4.in", 'r')

def find_next_letter(curr_letter):
    if curr_letter == 'X':
        return 'M'
    if curr_letter == 'M':
        return 'A'
    if curr_letter == 'A':
        return 'S'
    if curr_letter == 'S':
        return True

def check_for_xmas(grid, next_letter, curr_pos, direction):
    if (curr_pos[0] + direction[0] < 0) or (curr_pos[0] + direction[0] >= len(grid[0])):
        return False
    if (curr_pos[1] + direction[1] < 0) or (curr_pos[1] + direction[1] >= len(grid)):
        return False
    new_pos = []
    new_pos.append(curr_pos[0] + direction[0])
    new_pos.append(curr_pos[1] + direction[1])
    if grid[new_pos[0]][new_pos[1]] == next_letter:
        next_letter = find_next_letter(next_letter)
        if next_letter == True:
            return True
        else:
            return check_for_xmas(grid, next_letter, new_pos, direction)
    return False

def check_around(grid, curr_pos):
    result = 0
    if check_for_xmas(grid, 'M', curr_pos, [-1, -1]):
        result += 1
    if check_for_xmas(grid, 'M', curr_pos, [-1, 0]):
        result += 1
    if check_for_xmas(grid, 'M', curr_pos, [-1, 1]):
        result += 1
    if check_for_xmas(grid, 'M', curr_pos, [0, -1]):
        result += 1
    if check_for_xmas(grid, 'M', curr_pos, [0, 1]):
        result += 1
    if check_for_xmas(grid, 'M', curr_pos, [1, -1]):
        result += 1
    if check_for_xmas(grid, 'M', curr_pos, [1, 0]):
        result += 1
    if check_for_xmas(grid, 'M', curr_pos, [1, 1]):
        result += 1
    return result

word_search = []
for i in f:
    row = []
    for j in i:
        if j != "\n":
            row.append(j)
    word_search.append(row)

result = 0
for i in range(0, len(word_search)):
    for j in range(0, len(word_search[i])):
        if word_search[i][j] == 'X':
            result += check_around(word_search, [i, j])

print(result)

# part 2

def check_for_crossmas(grid, position):
    cross_counter = 0
    top_left = [position[0]-1, position[1]-1]
    top_right = [position[0]-1, position[1]+1]
    bottom_left = [position[0]+1, position[1]-1]
    bottom_right = [position[0]+1, position[1]+1]

    if grid[top_left[0]][top_left[1]] == 'M' and grid[bottom_right[0]][bottom_right[1]] == 'S':
        cross_counter += 1
    if grid[top_right[0]][top_right[1]] == 'M' and grid[bottom_left[0]][bottom_left[1]] == 'S':
        cross_counter += 1
    if grid[bottom_left[0]][bottom_left[1]] == 'M' and grid[top_right[0]][top_right[1]] == 'S':
        cross_counter += 1
    if grid[bottom_right[0]][bottom_right[1]] == 'M' and grid[top_left[0]][top_left[1]] == 'S':
        cross_counter += 1
    if cross_counter == 2:
        return True
    return False

result = 0
for i in range(1, len(word_search)-1):
    for j in range(1, len(word_search[i])-1):
        if word_search[i][j] == 'A':
            if check_for_crossmas(word_search, [i, j]):
                result += 1
print(result)