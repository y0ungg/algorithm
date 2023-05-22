from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
g = []
for _ in range(N):
  g.append(input().strip())

delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def bfs(start):
  q = deque()
  q.append(start)
  visited = [[0 for _ in range(M)] for _ in range(N)]
  visited[start[0]][start[1]] = 1
  max_res = 0
  while q:
    hx, hy = q.popleft()
    for dx, dy in delta:
      x, y = hx + dx, hy + dy
      if 0 <= x < N and 0 <= y < M and not visited[x][y]:
        if g[x][y] == "W":
          visited[x][y] = -1
        else:
          visited[x][y] = visited[hx][hy] + 1
          max_res = max(max_res, visited[x][y] - 1)
          q.append((x, y))
  return max_res
  
result = 0
for i in range(N):
  for j in range(M):
    if g[i][j] == "L":
      result = max(result, bfs((i, j)))
print(result)