with open(r"input.txt") as f:
    total = 0
    for line in f.readlines():
        val = int(line)
        while val > 0:
            val = int(val/3.)
            val -= 2
            total += val
            if (int(val/3.) - 2) <= 0:
                break
    print(total)
