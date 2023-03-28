import sys
input = sys.stdin.readline
total = int(input())
C = int(input())
l = []
target = set([])
for i in range(C):
  a = list(map(int, input().split()))
  if a[0] == 1 and a[1] not in target:
    target.add(a[1])
  if a[1] == 1 and a[0] not in target:
    target.add(a[0])
  l.append(a)

j = 0
while j < len(l): 
  x = l[j][0]
  y = l[j][1]
  if x in target:
    if not y in target and y != 1:
      target.add(y)
      j = 0
      continue
  elif y in target:
    if not x in target and x != 1:
      target.add(x)
      j = 0
      continue
  j += 1

print(len(target))