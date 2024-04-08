import sys
from collections import deque
input = sys.stdin.readline
q = deque()

M, N, H = map(int, input().split())
g = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
#아래, 위, 왼쪽, 오른쪽, 앞, 뒤
#z, x, y
delta = [(-1, 0, 0), (1, 0, 0), (0, 0, -1), (0, 0, 1), (0, 1, 0), (0, -1, 0)]

def bfs():
  while q:
    z, x, y = q.popleft()
    for dz, dx, dy in delta:
      nz, nx, ny = z + dz, x + dx, y + dy
      if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M:
        if g[nz][nx][ny] == 0:
          g[nz][nx][ny] = g[z][x][y] + 1
          q.append((nz, nx, ny))

        
for i in range(H):
  for j in range(N):
    for k in range(M):
      if g[i][j][k] == 1:
        q.append((i, j, k))
        
bfs()
     
cannot = False
days = 0

for i in range(H):
  for j in range(N):
    for k in range(M):
      if g[i][j][k] == 0:
        cannot = True
        break
      days = max(days, g[i][j][k] - 1)

if cannot:
  print(-1)
else:
  print(days)
