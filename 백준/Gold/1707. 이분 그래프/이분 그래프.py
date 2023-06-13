from collections import deque
import sys
input = sys.stdin.readline
def bfs(start):
  global V, flag, visited
  visited[start] = 1
  q = deque()
  q.append(start)
  while q:
    here = q.popleft()
    color = 1 if visited[here] == 2 else 2
    for edge in vertex[here]:
      if not visited[edge]:
        visited[edge] = color
        q.append(edge)
      elif visited[edge] == visited[here]:
        flag = 1
        break
  return

K = int(input())
for _ in range(K):
  V, E = map(int, input().split())
  vertex = [[] for _ in range(V + 1)]
  visited = [0 for _ in range(V + 1)]
  flag = 0
  for _ in range(E):
    a, b = map(int, input().split())
    vertex[a].append(b)
    vertex[b].append(a)
  for v in range(1, V+1):
    if not flag and not visited[v]:
      bfs(v)
  print("YES" if not flag else "NO")