import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N - 1):
  a, b, c = map(int, input().split())
  tree[a].append((b, c))
  tree[b].append((a, c))

distance = [-1 for _ in range(N+1)]
distance[1] = 0
def dfs(here, weight):
  for node, w in tree[here]:
    if distance[node] == -1:
      distance[node] = w + weight
      dfs(node, w + weight)
dfs(1, 0)

idx = distance.index(max(distance))
distance = [-1 for _ in range(N+1)]
distance[idx] = 0
dfs(idx, 0)
print(max(distance))