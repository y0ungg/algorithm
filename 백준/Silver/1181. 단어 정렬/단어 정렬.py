N = int(input())
l = []

for i in range(N):
  x = str(input())
  if l.count(x) > 0:
    continue
  else: l.append(x)

s = sorted(l, key=lambda x: (len(x), x))

for word in s:
  print(word)