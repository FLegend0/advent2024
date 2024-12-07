import re
f = open('day3.in','r')

def search_for_muls(i):
    result = 0
    matches = re.findall("mul([0-9]{1,3},[0-9]{1,3})", i)
    for j in matches:
        numbers = re.findall("[0-9]+", j)
        result += int(numbers[0]) * int(numbers[1])
    return result

result = 0
for i in f:
    result += search_for_muls(i)

print(result)

f = open('day3.in','r')

enabled = True
full_string = ""
result = 0
for i in f:
    full_string += i

dont_split = re.split("don\'t()", full_string)
print(len(dont_split))
for i in dont_split:
    if enabled:
        result += search_for_muls(i)
        enabled = False
    else:
        sorted_split = re.split("do()", i)
        if len(sorted_split) > 1:
            for j in range(1, len(sorted_split)):
                result += search_for_muls(sorted_split[j])

print(result)