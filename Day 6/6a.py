with open(r"input") as f:
    file = f.readlines()
    relations = {}
    for relation in file:
        orbits = relation.split(")")
        relations[orbits[1].rstrip()] = orbits[0]
    print(relations)
    indirect = 0
    for obj in relations.keys():
        key = obj
        while key in relations.keys():
            indirect += 1
            key = relations[key]
    print(indirect)
        
        