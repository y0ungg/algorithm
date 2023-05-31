from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
g, blank, virus = [], [], []
for i in range(N):
  g.append(list(map(int, input().split())))
  for j in range(M):
    if not g[i][j]: blank.append((i, j))
    if g[i][j] == 2: virus.append((i, j))

delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def bfs(graph):
  q = deque()
  q.append(virus[0])
  visited = [[0 for _ in range(M)] for _ in range(N)]
  visited[virus[0][0]][virus[0][1]] = 1
  while q:
    hx, hy = q.popleft()
    for dx, dy in delta:
      nx, ny = dx + hx, dy + hy
      if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
        if not graph[nx][ny] or graph[nx][ny] == 2:
          visited[nx][ny] = 1
          graph[nx][ny] = 3
          q.append((nx, ny))        
    for x, y in virus:
      if not visited[x][y]:
        visited[x][y] = 1
        q.append((x, y)) 
  total = 0
  for row in graph:
    for cur in row:
      if not cur: total += 1
  return total

result = 0
def make_walls(arr, depth):
  global result
  if depth == 3:
    copied = [row[:] for row in g]
    for cur in arr:
      copied[blank[cur][0]][blank[cur][1]] = 1
    result = max(result, bfs(copied))
    return
  for i in range(len(blank)):
    if not len(arr) or arr[-1] < i:
      arr.append(i)
      make_walls(arr, depth + 1)
      arr.pop()
      
make_walls([], 0)
print(result)
    