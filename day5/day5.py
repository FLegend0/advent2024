f = open('day5.in', 'r')

def check_order(rules, value, checked):
    if value in rules:
        for k in rules[value]:
            if k in checked:
                return False
    return True

def reorder(rules, page):
    checked = []
    for i in page:
        if not check_order(rules, i, checked):
            index = len(checked) - 1
            sortchecked = checked[:index]
            while not check_order(rules, i, sortchecked):
                index -= 1
                sortchecked = checked[:index]
            checked.insert(index, i)
        else:
            checked.append(i)
    return checked

rules = {}
pages = False
result = 0
result_incorrect_order = 0
for i in f:
    i = i.strip()
    if i == '':
        pages = True
        continue
    if not pages:
        rule = i.split("|")
        if rule[0] not in rules:
            rules[rule[0]] = []
        rules[rule[0]].append(rule[1])

    else:
        page = i.split(",")
        valid = True
        checked = []
        for j in page:
            if not check_order(rules, j, checked):
                valid = False
                break
            checked.append(j)
        
        if valid:
            middle = len(page) // 2
            result += int(page[middle])
        else:
            newpage = reorder(rules, page)
            middle = len(newpage) // 2
            result_incorrect_order += int(newpage[middle])
            
print(result)
print(result_incorrect_order)

        
            
    