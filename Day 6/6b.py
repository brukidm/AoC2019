with open(r"input") as f:
    file = f.readlines()
    relations = {}
    for relation in file:
        orbits = relation.split(")")
        relations[orbits[1].rstrip()] = orbits[0]
    steps = 0
    you_to_com = []
    san_to_com = []  
    key = "YOU"   
    while key != "COM":
        you_to_com.append(relations[key])
        key = relations[key]
    key = "SAN"
    while key != "COM":
        san_to_com.append(relations[key])
        key = relations[key]         
    you_to_com = set(you_to_com)
    san_to_com = set(san_to_com)
    print(len(you_to_com ^ san_to_com))