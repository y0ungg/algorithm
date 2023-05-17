import sys
input = sys.stdin.readline

N, M = map(int, input().split())
g = []
for _ in range(N):
  g.append(list(map(int, input().split())))

home = []
chicken = []
for i in range(N):
  for j in range(N):
    if g[i][j] == 1:
      home.append((i + 1, j + 1))
    if g[i][j] == 2:
      chicken.append((i + 1, j + 1))

total = []
for h in home:
  temp = []
  hx, hy = h
  for c in chicken:
    cx, cy = c
    temp.append(abs(hx-cx) + abs(hy-cy))
  total.append(temp)

min_res = 10000000000000
def do(arr, depth):
  global min_res
  if depth > M:
    return
  res = 0
  for i in range(len(home)):
    temp = 1001
    for x in arr:
      temp = min(temp, total[i][x])
    res += temp
  min_res = min(min_res, res)
  for j in range(len(chicken)):
    if len(arr) == 0 or arr[-1] < j:
      arr.append(j)
      do(arr, depth + 1)
      arr.pop()
        
do([], 0)
print(min_res)