import re
counter = 0
for password in range(109165, 576723):
  adjacent = False
  decreasing = False
  stringified = str(password)
  if re.search(r"(.)\1", stringified):
    adjacent = True
  for i in range(6):
    for j in range(i, 6):
      if int(stringified[i]) > int(stringified[j]):
        decreasing = True
  if(adjacent and not decreasing):
    counter += 1
print(counter)  