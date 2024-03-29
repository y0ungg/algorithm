import sys
input = sys.stdin.readline
R, C = map(int, input().split())
g = [[*map(ord, input())] for _ in range(R)]

alphabet = [0 for _ in range(26)]
alphabet[g[0][0] - 65] = 1
delta = [(-1, 0), (0, -1), (0, 1), (1, 0)]
res, flag = 0, 0
def dfs(hx, hy, count):
  global res, flag
  res = max(res, count)
  if res == 26:
    flag = 1
    return
  for dx, dy in delta:
    nx, ny = hx + dx, hy + dy
    if 0 <= nx < R and 0 <= ny < C:
      if not alphabet[g[nx][ny] - 65] and not flag:
        alphabet[g[nx][ny] - 65] = 1
        dfs(nx, ny, count + 1)
        alphabet[g[nx][ny] - 65] = 0
dfs(0, 0, 1)
print(res)