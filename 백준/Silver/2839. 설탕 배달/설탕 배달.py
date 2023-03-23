T = int(input())
def calc():
  if T % 5 == 0:
    return print(T // 5)
  num = T % 5
  count = T // 5
  if num == 1 or num == 3:
    count += 1
  elif num == 2:
    if T >= 12:
      count += 2
    else: return print(-1)
  elif num == 4:
    if count == 0: return print(-1)
    count += 2

  print(count)
calc()