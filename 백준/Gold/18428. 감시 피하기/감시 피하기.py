import sys
input = sys.stdin.readline
N = int(input())
g = []
walls = []
teachers = []
for i in range(N):
  g.append(list(input().strip().split()))
  for j in range(N):
    if g[i][j] == "X":
      walls.append((i, j))
    elif g[i][j] == "T":
      teachers.append((i, j))

delta = [(-1, 0), (1, 0), (0, 1), (0, -1)]
answer = 0
def check(wall_arr):
  global answer
  for t in teachers:
    tx, ty = t
    for dx, dy in delta:
      for i in range(1, 6):
        nx, ny = tx + (dx * i), ty + (dy * i)
        if 0 <= nx < N and 0<= ny < N:
          if g[nx][ny] == "S":
            return 0
          elif (nx, ny) in wall_arr: break
  return 1

def make_walls(arr, cur):
  global answer
  if len(arr) == 3:
    answer = check(arr)
    return
  for i in range(len(walls)):
    if len(arr) == 0 or cur < i and not answer:
      arr.append((walls[i][0], walls[i][1]))
      make_walls(arr, i)
      arr.pop()
      
make_walls([], 0)
print("YES" if answer else "NO")