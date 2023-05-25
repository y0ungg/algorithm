import sys
input = sys.stdin.readline
N, M = map(int, input().split())
floor, move = [], []
for _ in range(N):
  floor.append(list(map(int, input().split())))

init_cloud = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]
way = [None, (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
delta = [(-1, -1), (1, 1), (-1, 1), (1, -1)]

def move_cloud(cloud, head, count):
  hx, hy = way[head]
  moved_cloud = []
  for x, y in cloud:
    nx, ny = (x + (hx * count)) % N, (y + (hy * count)) % N
    floor[nx][ny] += 1
    moved_cloud.append((nx, ny))
  for x, y in moved_cloud:
    baskets = 0
    for dx, dy in delta:
      nx, ny = x + dx, y + dy
      if 0 <= nx < N and 0 <= ny < N:
        if floor[nx][ny]: baskets += 1
    floor[x][y] += baskets
  new_cloud = []
  for i in range(N):
    for j in range(N):
      if floor[i][j] >= 2 and not (i, j) in moved_cloud:
        floor[i][j] -= 2
        new_cloud.append((i, j))
  return new_cloud

for _ in range(M):
  d, s = map(int, input().split())
  init_cloud = move_cloud(init_cloud, d, s)

total = 0
for x in range(N):
  for y in range(N):
    total += floor[x][y]
print(total)