from collections import deque
import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())
g = [[] for _ in range(N+1)]
for _ in range(M):
  a, b = map(int, input().split())
  g[a].append(b)
  g[b].append(a)

for i in range(len(g)):
  g[i] = sorted(g[i])

visited = [0 for _ in range(N+1)]
def dfs(here):
  if (visited[here]): return
  visited[here] = 1
  print(here, end=" ")
  for there in g[here]:
    dfs(there)

dfs(V)
print()

def bfs(start):
  q = deque()
  q.append(start)
  visited = [0 for _ in range(N+1)]
  visited[start] = 1
  while q:
    here = q.popleft()
    print(here, end=" ")
    for there in g[here]:
      if visited[there]: continue
      visited[there] = 1
      q.append(there)

bfs(V)
print()