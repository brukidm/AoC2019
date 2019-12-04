import re
counter = 0
for password in range(109165, 576723):
    appearances = {
        "0": [],
        "1": [],
        "2": [],
        "3": [],
        "4": [],
        "5": [],
        "6": [],
        "7": [],
        "8": [],
        "9": [],

    }
    adjacent = False
    decreasing = False
    stringified = str(password)
    for i in range(len(stringified)):
        appearances[stringified[i]].append(i)
    for list in appearances.values():
        if len(list) == 2:
            adjacent = True
    for i in range(6):
        for j in range(i, 6):
            if int(stringified[i]) > int(stringified[j]):
                decreasing = True
    if(adjacent and not decreasing):
        counter += 1
print(counter) 