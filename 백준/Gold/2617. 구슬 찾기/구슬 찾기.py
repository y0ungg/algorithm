from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
center = (N + 1) // 2
light_balls = [[] for _ in range(N + 1)]
heavy_balls = [[] for _ in range(N + 1)]
for _ in range(M):
  a, b = map(int, input().split())
  light_balls[a].append(b)
  heavy_balls[b].append(a)

answer = 0
def bfs(start):
  global answer
  visited = [0 for _ in range(N + 1)]
  visited[start] = 1
  q = deque()
  q.append(start)
  count = 0
  while q:
    here = q.popleft()
    for cur in light_balls[here]:
      if visited[cur]: continue
      visited[cur] = 1
      count += 1
      q.append(cur)
  if count >= center:
    answer += 1
    return
  visited = [0 for _ in range(N + 1)]
  visited[start] = 1
  q.append(start)
  count = 0
  while q:
    here = q.popleft()
    for cur in heavy_balls[here]:
      if visited[cur]: continue
      visited[cur] = 1
      count += 1
      q.append(cur)
  if count >= center:
    answer += 1
    return
    
for i in range(1, N+1):
  bfs(i)
print(answer)