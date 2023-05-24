import sys
input = sys.stdin.readline
N, M = map(int, input().split())
g = []
for i in range(N):
  g.append(list(map(int, input().strip())))

big_num = -1
def dfs(i, j):
  global big_num
  for ox in range(-N, N):
    for oy in range(-M, M):
      if ox == 0 and oy == 0: continue
      num = g[i][j]
      nx, ny = i + ox, j + oy
      while 0 <= nx < N and 0 <= ny < M:
        num = (num * 10) + g[nx][ny]
        tmp = int(num ** 0.5)
        if tmp ** 2 == num:
          big_num = max(big_num, num)
        nx += ox
        ny += oy
      tmp = int(num ** 0.5)
      if tmp ** 2 == num:
        big_num = max(big_num, num)
      
for i in range(N):
  for j in range(M):
    dfs(i, j)
print(big_num)