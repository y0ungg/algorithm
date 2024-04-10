import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(N)]

delta = [(0, 1), (1, 0), (-1, 0), (0, -1)]

v = []
num = 0
for i in range(N):
  for j in range(N):
    if g[i][j] == 2:
      v.append((i, j))
    if not g[i][j]:
      num += 1
      
visited = [0] * 11
ms = 0xfffff

def solve(arr, d):
  global ms
  if (len(arr) == M):
    ss = bfs(arr)
    if ss != -1:
      ms = min(ms, ss)
    return
  if d < len(v):
    arr.append(v[d])
    solve(arr, d+1)
    arr.pop()
    solve(arr, d+1)

def bfs(arr):
  global num, ms
  num_g = 0
  s = 0
  visited_g = [[-1] * N for _ in range(N)]
  for vv in arr:
    vx, vy = vv
    visited_g[vx][vy] = 0
  q = deque(arr)
  while q:
    x, y = q.popleft()
    if ms <= s:
      return ms
    for dx, dy in delta:
      nx, ny = x + dx, y + dy
      if 0 <= nx < N and 0 <= ny < N:
        if visited_g[nx][ny] == -1 and g[nx][ny] != 1:
          if g[nx][ny] == 0:
            s = max(s, visited_g[x][y] + 1)
            num_g += 1
          visited_g[nx][ny] = visited_g[x][y] + 1
          q.append((nx, ny))
  if num_g == num:
    return s
  return -1
solve([], 0)
if ms == 0xfffff:
  print(-1)
else: 
  print(ms)