with open(r"input.txt") as f:
    total = 0
    for line in f.readlines():
        val = int(line)
        val = int(val/3.)
        val -= 2
        total += val
    print(total)
