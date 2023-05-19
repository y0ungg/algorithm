from collections import deque
import sys
input = sys.stdin.readline
gears = []
for _ in range(4):
  gears.append(deque(input().strip()))

def do(num, way):
  q = deque()
  q.append(num)
  visited = [0, 0, 0, 0]
  visited[num] = 1
  todo = []
  while q:
    here = q.popleft()
    todo.append(here)
    left, right = here - 1, here + 1
    if right < 4 and not visited[right]:
      visited[right] = 1
      if gears[here][2] != gears[right][6]:
        q.append(right)
    if 0 <= left and not visited[left]: 
      visited[left] = 1
      if gears[here][6] != gears[left][2]:
        q.append(left)
  for target in todo:
    if target == num or abs(num - target) == 2:
      gears[target].rotate(way)
    else: gears[target].rotate(-1 * way)

N = int(input())
for _ in range(N):
  num, way = map(int, input().split())
  do(num - 1, way)
  
res = 0
cur = 1
for gear in gears:
  if gear[0] == "1":
    res += (1 * cur)
  cur *= 2

print(res)