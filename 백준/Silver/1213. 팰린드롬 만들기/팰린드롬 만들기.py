import sys 
input = sys.stdin.readline

S = sorted(str(input().rstrip()))
d = {}
for word in S:
  if not word in d:
    d[word] = 1
  else: d[word] += 1

flag = 0
center = ""
res = ""
for key, value in d.items():
  if value % 2:
    if not len(center):
      center = key
      d[key] = value - 1
    else:
      flag = 1
      print("I'm Sorry Hansoo")
      break
  res += key * (value // 2)

if not flag: print(res + center + res[::-1])