from collections import deque
import sys
input = sys.stdin.readline

N, L, R = map(int, input().split())
g = []
for _ in range(N):
  g.append(list(map(int, input().split())))

delta = [(-1, 0), (1, 0), (0, 1), (0, -1)]
def bfs(start):
  q = deque()
  q.append(start)
  union = [start]
  population = g[start[0]][start[1]]
  while q:
    hx, hy = q.popleft()
    for dx, dy in delta:
      x, y = hx + dx, hy + dy
      if 0 <= x < N and 0 <= y < N:
        if L <= abs(g[hx][hy] - g[x][y]) <= R and not visited[x][y]:
          visited[x][y] = 1
          population += g[x][y]
          q.append((x, y))
          union.append((x, y))
  return union, population

day = 0
while True:
  visited = [[0 for _ in range(N)] for _ in range(N)]
  moved = 0
  for i in range(N):
    for j in range(N):
      if not visited[i][j]:
        visited[i][j] = 1
        union, total = bfs((i, j))
        if len(union) > 1:
          average = total // len(union)
          for x, y in union:
            g[x][y] = average
          moved = 1
  if not moved:
      break
  day += 1

print(day)