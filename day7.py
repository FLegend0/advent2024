f = open('day7.in', 'r')

# Part 1 OLD FUNCTION HAHAHA LOOK AT THIS SHIT
def next_operation(operations):
    plus_count = operations.count('+')
    if plus_count == len(operations):
        return False
    if plus_count > 0 and operations[-1] != '+':
        currindex = ''.join(operations).rindex('+')
        operations[currindex] = 'x'
        operations[currindex+1] = '+'
    elif plus_count == 0:
        plus_count = 1
        operations = (['+']*plus_count) + (['x']*(len(operations) - plus_count))
    else:
        # find next + and move it forward if possible
        currindex = ''.join(operations).rindex('+')
        currplus = 2
        addnew = True
        while currplus <= plus_count:
            nextindex = ''.join(operations[:currindex]).rindex('+')
            if nextindex + 1 == currindex:
                currplus += 1
                currindex = nextindex
                continue
            operations[nextindex] = 'x'
            operations[nextindex+1] = '+'
            tempplus = currplus-1
            for i in range(nextindex+2, len(operations)):
                if tempplus > 0:
                    operations[i] = '+'
                    tempplus -= 1
                else:
                    operations[i] = 'x'
            currindex = nextindex
            addnew = False
            break

        if addnew:
            plus_count += 1
            operations = (['+']*plus_count) + (['x']*(len(operations) - plus_count))

    return operations

# part 1 NEW function
def binary(n, size):
    nums = []
    while n:
        n, r = divmod(n, 2)
        nums.insert(0, r)
    if len(nums) > size:
        return False
    while len(nums) < size:
        nums.insert(0, 0)
    
    for i in range(0, len(nums)):
        if nums[i] == 0:
            nums[i] = 'x'
        elif nums[i] == 1:
            nums[i] = '+'
        elif nums[i] == 2:
            nums[i] = '|'
    return nums

# for part 2
def ternary(n, size):
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.insert(0, r)
    if len(nums) > size:
        return False
    while len(nums) < size:
        nums.insert(0, 0)
    
    for i in range(0, len(nums)):
        if nums[i] == 0:
            nums[i] = 'x'
        elif nums[i] == 1:
            nums[i] = '+'
        elif nums[i] == 2:
            nums[i] = '|'
    return nums

def calc(values):
    result = int(values[0])
    calcvalues = values[1:]
    n = 0

    # convert n into a set of operations

    # part 1
    # operations = binary(n, len(values)-2)  

    # part 2
    operations = ternary(n, len(values)-2)

    while operations != False:
        calculation = int(calcvalues[0])
        for i in range(0, len(operations)):
            if operations[i] == 'x':
                calculation *= int(calcvalues[i+1])
            elif operations[i] == '+':
                calculation += int(calcvalues[i+1])
            elif operations[i] == '|':
                calculation = int(str(calculation) + calcvalues[i+1])
        if calculation == result:
            return True

        # reconvert n into new operations
        n += 1

        # part 1
        # operations = binary(n, len(values)-2)

        # part 2
        
        operations = ternary(n, len(values)-2)
    
    return False

    
result = 0
for i in f:
    i = i.strip()
    values = i.split()
    values[0] = values[0][:-1]
    if calc(values):
        result += int(values[0])
print(result)