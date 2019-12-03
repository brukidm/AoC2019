import ast

with open(r"input") as f:
    file = f.readlines()
    positions = {}
    counter = 0
    for wire in file:
        moves = wire.split(",")
        positions[counter] = set()
        location = [0, 0]
        for move in moves:
            length = int(move[1:])
            if move[0] == "R":
                for _ in range(length):
                    location[0] = location[0] + 1
                    positions[counter].add(str(location))
            elif move[0] == "L":
                for _ in range(length):
                    location[0] = location[0] - 1
                    positions[counter].add(str(location))
            elif move[0] == "U":
                for _ in range(length):
                    location[1] = location[1] + 1
                    positions[counter].add(str(location))
            else:
                for _ in range(length):
                    location[1] = location[1] - 1
                    positions[counter].add(str(location))
        counter += 1
    distances = set()
    intersections = positions[0].intersection(positions[1])
    for intersection in intersections:
        coords = ast.literal_eval(intersection)
        distances.add((abs(int(coords[0])) + abs(int(coords[1]))))
    print(min(distances))