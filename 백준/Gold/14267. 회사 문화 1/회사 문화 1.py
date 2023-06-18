import sys
input = sys.stdin.readline
N, M = map(int, input().split())
tmp = [*map(int, input().split())]
people = [[] for _ in range(N + 1)]
for i in range(1, N):
  people[tmp[i]].append(i + 1)
  
praise = [0 for _ in range(N + 1)]
for _ in range(M):
  a, b = map(int, input().split())
  praise[a] += b

for i in range(2, N):
  if not praise[i]: continue
  for bottom in people[i]:
    praise[bottom] += praise[i]
print(*praise[1:])