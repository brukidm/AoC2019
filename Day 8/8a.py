with open(r"input") as f:
    file = f.readline()[:-1]
    layer = 1
    layers = {}
    numbers_read = 0
    for digit in file:
        if numbers_read == 150:
            numbers_read = 0
            layer += 1
        if layer not in layers.keys():
            layers[layer] = [digit]
            numbers_read += 1
        else:
            layers[layer].append(digit)
            numbers_read += 1
    min = 150
    for key in layers.keys():
        layer = layers[key]
        zeroes = 0
        for digit in layer:
            if digit == "0":
                zeroes += 1
        if zeroes < min:
            min = zeroes
            lowest = key
    ones = 0
    twos = 0
    for digit in layers[lowest]:
        if digit == "1":
            ones += 1
        if digit == "2":
            twos += 1
    print(ones*twos)