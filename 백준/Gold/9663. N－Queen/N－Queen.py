import sys
input = sys.stdin.readline
N = int(input())
count = 0
chess = [0 for _ in range(N+1)]
def dfs(depth):
  global count
  if depth == N + 1:
    count += 1
    return
  for i in range(N):
    flag = 0
    if chess[i]: continue
    for j in range(depth, 0, -1):
      a, b = i + (depth - j), i - (depth - j)
      if (0 <= a < N and chess[a] == j) or (0 <= b < N and chess[b] == j): flag = 1
    if not flag:
      chess[i] = depth
      dfs(depth + 1)
      chess[i] = 0
  
dfs(1)
print(count)