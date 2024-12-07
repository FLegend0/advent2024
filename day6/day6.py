f = open('day6.in', 'r')

looppaths = 0

def is_guard(tile):
    if tile == '^':
        return 'UP'
    elif tile == '>':
        return 'RIGHT'
    elif tile == 'v':
        return 'DOWN'
    elif tile == '<':
        return 'LEFT'
    else:
        return False

def rotate(tile):
    if tile == '^':
        return '>'
    elif tile == '>':
        return 'v'
    elif tile == 'v':
        return '<'
    elif tile == '<':
        return '^'
    else:
        return False


def traverse_path(lab, currpos):
    tile = lab[currpos[0]][currpos[1]]
    direction = is_guard(tile)
    newpos = currpos.copy()
    if direction == 'UP':
        newpos[0] -= 1
    elif direction == 'RIGHT':
        newpos[1] += 1
    elif direction == 'DOWN':
        newpos[0] += 1
    elif direction == 'LEFT':
        newpos[1] -= 1

    if newpos[0] < 0 or newpos[0] >= len(lab):
        lab[currpos[0]][currpos[1]] = 'X'
        return True
    if newpos[1] < 0 or newpos[1] >= len(lab[0]):
        lab[currpos[0]][currpos[1]] = 'X'
        return True
    
    if lab[newpos[0]][newpos[1]] != '#':

        # part 1 stuff
        lab[currpos[0]][currpos[1]] = 'X'
        lab[newpos[0]][newpos[1]] = tile
        currpos[0] = newpos[0]
        currpos[1] = newpos[1]
    else:
        newtile = rotate(tile)
        lab[currpos[0]][currpos[1]] = newtile
    return False

def traverse_path_part2(lab, currpos):
    tile = lab[currpos[0]][currpos[1]][0]
    direction = is_guard(tile)
    newpos = currpos.copy()
    if direction == 'UP':
        newpos[0] -= 1
    elif direction == 'RIGHT':
        newpos[1] += 1
    elif direction == 'DOWN':
        newpos[0] += 1
    elif direction == 'LEFT':
        newpos[1] -= 1

    if newpos[0] < 0 or newpos[0] >= len(lab):
        return True
    if newpos[1] < 0 or newpos[1] >= len(lab[0]):
        return True
    
    if lab[newpos[0]][newpos[1]][0] != '#':
        temptile = rotate(tile)
        if temptile in lab[currpos[0]][currpos[1]]:
            global looppaths
            looppaths += 1

        if '.' in lab[newpos[0]][newpos[1]]:
            lab[newpos[0]][newpos[1]].remove('.')
        lab[newpos[0]][newpos[1]].insert(0, tile)
        currpos[0] = newpos[0]
        currpos[1] = newpos[1]
    else:
        newtile = rotate(tile)
        lab[currpos[0]][currpos[1]].insert(0, newtile)
    return False


lab = []
guardpos = [0, 0] # [row, col]
currow = 0
for i in f:
    i = i.strip()
    row = []
    for j in i:
        if is_guard(j) != False:
            guardpos = [currow, len(row)]
        row.append(j)
        
    lab.append(row)
    currow += 1

while not traverse_path(lab, guardpos):
    pass

xcount = 0
for i in lab:
    for j in i:
        if j == 'X':
            xcount += 1
print(xcount)

# part2
f = open('day6.in', 'r')
lab = []
guardpos = [0, 0] # [row, col]
currow = 0
for i in f:
    i = i.strip()
    row = []
    for j in i:
        if is_guard(j) != False:
            guardpos = [currow, len(row)]
        temp = []
        temp.append(j)
        row.append(temp)
        
    lab.append(row)
    currow += 1

while not traverse_path_part2(lab, guardpos):
    pass
print(looppaths)