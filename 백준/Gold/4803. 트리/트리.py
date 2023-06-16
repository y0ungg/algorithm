from collections import deque
import sys
input = sys.stdin.readline
def bfs(start):
  global count, visited
  q = deque()
  q.append(start)
  flag = 0
  while q:
    here = q.popleft()
    if visited[here]: flag = 1
    visited[here] = 1
    for edge in vertex[here]:
      if not visited[edge]:
        q.append(edge)
  if not flag: count += 1

case_cnt = 0
while 1:
  count = 0
  case_cnt += 1
  N, M = map(int, input().split())
  if not N and not M: break
  visited = [0 for _ in range(N + 1)]
  vertex = [[] for _ in range(N + 1)]
  for _ in range(M):
    a, b = map(int, input().split())
    vertex[a].append(b)
    vertex[b].append(a)
  for v in range(1, N + 1):
    if not visited[v]:
      bfs(v)
  if not count: print(f"Case {case_cnt}: No trees.")
  elif count == 1: print(f"Case {case_cnt}: There is one tree.")
  else: print(f"Case {case_cnt}: A forest of {count} trees.")