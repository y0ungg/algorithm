import sys
input = sys.stdin.readline

N = int(input())
score = []
for _ in range(N):
  score.append(list(map(int, input().split())))

members = [i for i in range(N)]
ans = 999999999999
def check(arr):
  global ans
  total_start = 0
  total_link = 0
  link = list(set(members) - set(arr))
  for x in arr:
    for y in arr:
      total_start += score[x][y]
  for x in link:
    for y in link:
      total_link += score[x][y]
  ans = min(ans, abs(total_start - total_link))
      
visited = [False] * N
def team(start, count):
  if count == N // 2:
    check(start)
    return
  for i in range(N):
    if not visited[i]:
      if len(start) == 0 or start[-1] < i:
        visited[i] = True
        start.append(i)
        team(start, count + 1)
        start.pop()
        visited[i] = False

team([], 0)
print(ans)