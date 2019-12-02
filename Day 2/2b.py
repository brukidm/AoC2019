with open(r"input") as f:
  file = f.readline()
  for x in range(100):
    for y in range(100):
      codes = list(eval(file))
      codes[1] = x
      codes[2] = y
      for i in range(0, len(codes)-1, 4):
        if codes[i] == 99:
          break
        if codes[i] == 1:
          codes[codes[i+3]] = codes[codes[i+1]] + codes[codes[i+2]]
        elif codes[i] == 2:
          codes[codes[i+3]] = codes[codes[i+1]] * codes[codes[i+2]]
      if(codes[0] == 19690720):
        print(x, y)