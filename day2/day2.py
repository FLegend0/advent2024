def check_asc_or_desc(list):
    ascending = True
    if int(list[0]) - int(list[1]) < 0:
        ascending = True
    elif int(list[0]) - int(list[1]) > 0:
        ascending = False
    else:
        return False
    
    for i in range(1, len(list)):
        if ascending:
            if int(list[i-1]) - int(list[i]) >= 0:
                return False
        else:
            if int(list[i-1]) - int(list[i]) <= 0:
                return False
            
    return True

def check_if_within_safety(i):
    for j in range(1, len(i)):
        safety = abs(int(i[j-1]) - int(i[j]))
        if safety > 3 or safety < 1:
            return False
    return True

f = open('day2.in', 'r')

safe_count = 0
for i in f:
    i = i.split()
    safe = True
    if not check_asc_or_desc(i):
        continue
    if check_if_within_safety(i):
        safe_count += 1

print(safe_count)

# part 2
def check_asc_or_desc_areas(list):
    ascend_count = 0
    descend_count = 0
    
    for i in range(1, len(list)):
        if int(list[i-1]) - int(list[i]) < 0:
            ascend_count += 1
        elif int(list[i-1]) - int(list[i]) > 0:
            descend_count += 1
        else:
            return [i-1, i] # if value is same, return value
    if ascend_count == 0 or descend_count == 0:
        return True # no anomalies
    if ascend_count > 1 and descend_count > 1:
        return False # impossible
    ascending = True
    if ascend_count < descend_count:
        ascending = False
    for i in range(1, len(list)):
        if ascending:
            if int(list[i-1]) - int(list[i]) > 0:
                return [i-1, i]
        else:
            if int(list[i-1]) - int(list[i]) < 0:
                return [i-1, i]

def check_if_within_safety_modified(i):
    for j in range(1, len(i)):
        safety = abs(int(i[j-1]) - int(i[j]))
        if safety > 3 or safety < 1:
            return [j-1, j]
    return True

f = open('day2.in', 'r')
safe_count = 0
for i in f:
    i = i.split()
    safe = True
    judgement = check_asc_or_desc_areas(i)
    # print(judgement)
    if judgement == False:
        continue
    # 2nd checking
    if judgement == True:
        new_judgement = check_if_within_safety_modified(i)
        if new_judgement == True:
            safe_count += 1
        else:
            remodelled = i.copy()
            del remodelled[new_judgement[0]]
            if check_asc_or_desc(remodelled) and check_if_within_safety(remodelled):
                safe_count += 1
            else:
                remodelled = i.copy()
                del remodelled[new_judgement[1]]
                if check_asc_or_desc(remodelled) and check_if_within_safety(remodelled):
                    safe_count += 1
    else:
        remodelled = i.copy()
        del remodelled[judgement[0]]
        if check_asc_or_desc(remodelled) and check_if_within_safety(remodelled):
            safe_count += 1
        else:
            remodelled = i.copy()
            del remodelled[judgement[1]]
            if check_asc_or_desc(remodelled) and check_if_within_safety(remodelled):
                safe_count += 1
print(safe_count)
