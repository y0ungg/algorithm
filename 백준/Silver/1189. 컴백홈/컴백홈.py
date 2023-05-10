import sys 
input = sys.stdin.readline

N, M, K = map(int, input().split())
route = []
for _ in range(N):
  route.append(input())

count = 0
visited = [[0 for _ in range(M)] for _ in range(N)]
visited[N-1][0] = 1
delta = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def do(cur, depth):
  global count
  if depth == K and cur == (0, M-1):
    count += 1
    return
  if depth == K:
    return
  cx, cy = cur
  for dx, dy in delta:
    nx, ny = dx + cx, dy + cy
    if 0 <= nx < N and 0 <= ny < M and route[nx][ny] != "T":
      if visited[nx][ny]: continue
      visited[nx][ny] = 1
      do((nx, ny), depth + 1)
      visited[nx][ny] = 0

do((N-1, 0), 1)
print(count)