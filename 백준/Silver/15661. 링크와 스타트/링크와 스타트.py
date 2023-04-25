import sys 
input = sys.stdin.readline

N = int(input())
score = []
for _ in range(N):
  score.append(list(map(int, input().split())))

members = [i for i in range(N)]
min_gap = 2000
def calc(arr):
  global min_gap
  total_start = 0
  total_link = 0
  link = list(set(members) - set(arr))
  for x in arr:
    for y in arr:
      total_start += score[x][y]
  for x in link:
    for y in link:
      total_link += score[x][y]
  min_gap = min(min_gap, abs(total_start - total_link))

def team(arr):
  calc(arr)
  for i in range(N):
    if arr[-1] < i:
      arr.append(i)
      team(arr)
      arr.pop()
      
for i in range(N):
  team([i])

print(min_gap)