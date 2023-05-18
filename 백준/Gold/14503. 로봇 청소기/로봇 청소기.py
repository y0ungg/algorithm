from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
g = []
for _ in range(N):
  g.append(list(map(int, input().split())))
delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
back = [(1, 0), (0, -1), (-1, 0), (0, 1)]

def bfs(start, head):
  q = deque()
  q.append(start)
  while q:
    hx, hy = q.popleft()
    g[hx][hy] = 2
    flag = 0
    for dx, dy in delta:
      x, y = hx + dx, hy + dy
      if 0 <= x < N and 0 <= y < M:
        if g[x][y] == 0 and not flag:
          flag = 1
          head = (head - 1) % 4
          a, b = delta[head]
          nx, ny = hx + a, hy + b
          if g[nx][ny] == 0:
            q.append((nx, ny))
          else: q.append((hx, hy))
    if not flag:
      a, b = back[head]
      nx, ny = hx + a, hy + b
      if 0 <= nx < N and 0 <= ny < M and g[nx][ny] != 1:
        q.append((nx, ny))
      else: break
  return

bfs((r, c), d)
count = 0
for row in g:
  for r in row:
    if r == 2:
      count += 1
print(count)