import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
l = []
for _ in range(N):
  l.append(list(map(int, input().split())))

delta = [(-1, -1), (-1, 0), (0, -1), (1, 0), (0, 1), (1, 1), (1, -1), (-1, 1)]
def bfs(start):
  if l[start[0]][start[1]] == 1:
    return 0
  dists = []
  q = deque()
  q.append(start)
  visited = [[0 for _ in range(M)] for _ in range(N)]
  visited[start[0]][start[1]] = 1
  while q:
    x, y = q.popleft()
    for dx, dy in delta:
      nx, ny = x + dx, y + dy
      if 0 <= nx < N and 0 <= ny < M:
        if not visited[nx][ny]:
          visited[nx][ny] = visited[x][y] + 1
          if l[nx][ny]:
            return visited[nx][ny] - 1
          q.append((nx, ny))

res = -1
for i in range(N):
  for j in range(M):
    res = max(res, bfs((i, j)))
print(res)