import sys
input = sys.stdin.readline

N = int(input())
food = []
for _ in range(N):
  food.append(list(map(int, input().split())))

gap = 100000000000
def calc(arr):
  global gap
  if len(arr) == 1:
    return
  cur_s = 1
  cur_b = 0
  for i in range(1, len(arr)):
    cur_s *= food[arr[i]][0]
    cur_b += food[arr[i]][1]
  cur_gap = abs(cur_s - cur_b)
  gap = min(gap, cur_gap)
    
visited = [False] * N
def make_arr(arr, count):
  calc(arr)
  for i in range(N):
    if not visited[i] and arr[-1] < i:
      visited[i] = True
      arr.append(i)
      make_arr(arr, count + 1)
      arr.pop()
      visited[i] = False

if N == 1:
  print(abs(food[0][0] - food[0][1]))
else:
  make_arr([-1], 1)
  print(gap)