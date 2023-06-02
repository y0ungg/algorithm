import sys
input = sys.stdin.readline
N, M = map(int, input().split())
g = []
cctv = []
for i in range(N):
  g.append(list(map(int, input().split())))
  for j in range(M):
    if 0 < g[i][j] < 6: cctv.append((g[i][j], i, j))

delta = [
  None,
  [[(-1, 0)], [(0, 1)], [(1, 0)], [(0, -1)]],
  [[(0, -1), (0, 1)], [(1, 0), (-1, 0)]],
  [[(-1, 0), (0, 1)], [(0, 1), (1, 0)], [(1, 0), (0, -1)], [(0, -1), (-1, 0)]],
  [[(-1, 0), (0, 1), (0, -1)], [(0, 1), (1, 0), (0, -1)], [(-1, 0), (0, 1), (1, 0)], 
   [(1, 0), (0, -1), (-1, 0)]],
  [[(-1, 0), (0, 1), (1, 0), (0, -1)]]
]
result = N * M
def check(arr):
  global result
  graph = [row[:] for row in g]
  for cur in range(len(arr)):
    num, i, j = cctv[cur]
    for dx, dy in delta[num][arr[cur]]:
      nx, ny = i + dx, j + dy
      while 0 <= nx < N and 0 <= ny < M:
        if graph[nx][ny] == 6: break
        graph[nx][ny] = 7
        nx += dx
        ny += dy
        
  total = 0
  for x in range(N):
    for y in range(M):
      if graph[x][y] == 0: total += 1
  result = min(result, total)
  return

way = [-1 for _ in range(len(cctv))]
def dfs(arr, depth):
  global result
  if depth == len(cctv):
    check(arr)
    return
  for i in range(depth, len(cctv)):
    num, x, y = cctv[i]
    for j in range(len(delta[num])):
      way[i] = j
      dfs(way, i + 1)
dfs([], 0)
print(result)

