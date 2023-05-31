import sys
input = sys.stdin.readline

N, M = map(int, input().split())
g = []
for _ in range(N):
  g.append(list(map(int, input().split())))
tetromino = [[(0, 1), (0, 2), (0, 3)], 
             [(1, 0), (2, 0), (3, 0)],
             [(0, 1), (1, 0), (1, 1)],
             [(1, 0), (2, 0), (2, 1)],
             [(0, 1), (0, 2), (1, 0)],
             [(0, 1), (1, 1), (2, 1)],
             [(0, 1), (0, 2), (-1, 2)],
             [(1, 0), (2, 0), (2, -1)],
             [(1, 0), (1, 1), (1, 2)],
             [(0, -1), (1, -1), (2, -1)],
             [(0, 1), (0, 2), (1, 2)],
             [(1, 0), (1, 1), (2, 1)],
             [(0, 1), (-1, 1), (-1, 2)],
             [(-1, 0), (-1, 1), (-2, 1)],
             [(0, 1), (1, 1), (1, 2)],
             [(0, 1), (0, 2), (1, 1)],
             [(0, 1), (1, 1), (-1, 1)],
             [(0, 1), (0, 2), (-1, 1)],
             [(1, 0), (1, 1), (2, 0)]]

score = 0
def dfs(i, j):
  global score
  for row in tetromino:
    tmp = g[i][j]
    flag = 0
    for tx, ty in row:
      nx, ny = i + tx, j + ty
      if 0 <= nx < N and 0 <= ny < M:
        tmp += g[nx][ny]
      else:
        flag = 1
        break
    if not flag: score = max(score, tmp)
  return
      
for i in range(N):
  for j in range(M):
    dfs(i, j)
print(score)