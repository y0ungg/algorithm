import sys
input = sys.stdin.readline
N, M = map(int, input().split())
board = [input().strip() for _ in range(N)]
delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def dfs(here, start, depth):
  global color, flag
  hx, hy = here
  for dx, dy in delta:
    nx, ny = hx + dx, hy + dy
    if 0 <= nx < N and 0 <= ny < M:
      if (nx, ny) == start and depth >= 4:
        flag = 1
        return
      if not visited[nx][ny] and board[nx][ny] == color and not flag:
        visited[nx][ny] = 1
        dfs((nx, ny), start, depth + 1)
        visited[nx][ny] = 0

flag = 0
for i in range(N):
  for j in range(M):
    if flag: break
    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[i][j] = 1
    color = board[i][j]
    dfs((i, j), (i, j), 1)
print("Yes" if flag else "No")