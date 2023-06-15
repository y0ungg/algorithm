from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
g = [[] for _ in range(N + 1)]
for _ in range(M):
  a, b = map(int, input().split())
  g[a].append(b)
S = int(input())
tmp = list(map(int, input().split()))
fans = [0 for _ in range(N + 1)]
for t in tmp:
  fans[t] = 1

def bfs():
  q = deque()
  q.append(1)
  while q:
    here = q.popleft()
    if fans[here]: continue
    if not len(g[here]): return True
    for edge in g[here]:
      if not fans[edge]:
        q.append(edge)
  return False


res = bfs()
print("yes" if res else "Yes")