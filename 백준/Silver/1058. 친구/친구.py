import sys
input = sys.stdin.readline
N = int(input())
friends = []
for _ in range(N):
  friends.append(str(input().rstrip()))

graph = [[] for _ in range(N)]
for i in range(N):
  for j in range(N):
    if friends[i][j] == "Y":
      graph[i].append(j)
      
res = 0
for i in range(N):
  count = set(graph[i])
  for friend in graph[i]:
    for x in graph[friend]:
      if not x == i:
        count.add(x)
  res = max(res, len(count))
print(res)