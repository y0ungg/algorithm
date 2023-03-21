str = input()
result = 0
idx = 0
dict = {"c=" : 1, "c-": 1, "dz=": 1, "d-": 1, "lj": 1, "nj": 1, "s=": 1, "z=": 1}

while idx < len(str):
  if idx +2 < len(str) and f"{str[idx]}{str[idx+1]}{str[idx+2]}" in dict:
    idx = idx + 3
  elif idx +1 < len(str) and f"{str[idx]}{str[idx+1]}" in dict:
    idx = idx + 2
  else: idx = idx + 1
  result += 1

print(result)