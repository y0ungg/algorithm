from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
g, virus = [], []
for i in range(N):
  g.append(list(map(int, input().split())))
  for j in range(N):
    if g[i][j] == 2: virus.append((i, j))

delta = [(-1, 0), (0, 1), (0, -1), (1, 0)]
def bfs(arr):
  a, b = virus[arr[0]][0], virus[arr[0]][1]
  visited = [[0 for _ in range(N)] for _ in range(N)]
  visited[a][b] = 1
  q = deque()
  q.append((a, b))
  while q:
    hx, hy = q.popleft()
    for dx, dy in delta:
      nx, ny = hx + dx, hy + dy
      if 0 <= nx < N and 0 <= ny < N:
        if g[nx][ny] == 1: continue
        if not visited[nx][ny]:
          q.append((nx, ny))
        if not visited[nx][ny] or visited[nx][ny] > visited[hx][hy] + 1:
          visited[nx][ny] = visited[hx][hy] + 1
    for cur in arr:
      if not visited[virus[cur][0]][virus[cur][1]] or visited[virus[cur][0]][virus[cur][1]] > 1:
        visited[virus[cur][0]][virus[cur][1]] = 1
        q.append((virus[cur][0], virus[cur][1]))
        
  tmp_max = 0
  for i in range(N):
    for j in range(N):
      if g[i][j] != 1 and not visited[i][j]: return 10000
    tmp_max = max(tmp_max, max(visited[i]) - 1)
  return tmp_max
      
result = 10000
def make_virus(arr, depth):
  global result
  if depth == M:
    result = min(result, bfs(arr))
    return
  for i in range(len(virus)):
    if not len(arr) or arr[-1] < i:
      arr.append(i)
      make_virus(arr, depth + 1)
      arr.pop()
make_virus([], 0)
print(result if result < 10000 else -1)