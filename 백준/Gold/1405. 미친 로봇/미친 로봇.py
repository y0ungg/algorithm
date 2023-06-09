import sys
input = sys.stdin.readline
K, E, W, S, N = map(int, input().split())
delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
way = [E, W, S, N]

simple = 0
def dfs(here, depth, per):
  global simple
  if depth == K:
    simple += per
    return
  for i in range(4):
    if not way[i]: continue
    nx, ny = here[0] + delta[i][0], here[1] + delta[i][1]
    if visited[nx][ny]: continue
    visited[nx][ny] = 1
    dfs((nx, ny), depth + 1, per * way[i] * 0.01)
    visited[nx][ny] = 0

visited = [[0 for _ in range(29)] for _ in range(29)]
visited[14][14] = 1
dfs((14, 14), 0, 1)
print(f'{simple:.10f}')
