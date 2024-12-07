f = open('day1.in', 'r')
list1 = []
list2 = []
for i in f:
    i = i.split()
    list1.append(i[0])
    list2.append(i[1])

list1.sort()
list2.sort()
total = 0

for i in range(0, len(list1)): 
    total += abs(int(list1[i]) - int(list2[i]))
print(total)

list2CountMap = {}
for i in list2:
    if i in list2CountMap:
        list2CountMap[i] = list2CountMap[i] + 1
    else:
        list2CountMap[i] = 1

total = 0
for i in list1:
    if i in list2CountMap:
        total += int(i) * list2CountMap[i]

print(total)