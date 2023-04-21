import sys
input = sys.stdin.readline

N = int(input())
matrix = []
for _ in range(N):
  matrix.append(list(map(int, input().split())))

min_total = 10000001
def calc(arr):
  global min_total
  total = 0
  for i in range(1, N):
    if matrix[arr[i-1]][arr[i]] == 0:
      return
    total += matrix[arr[i-1]][arr[i]]
  if matrix[arr[-1]][arr[0]] == 0:
    return
  total += matrix[arr[-1]][arr[0]]
  min_total = min(min_total, total)

visited = [False] * N
def make_route(arr, count):
  if count == N + 1:
    calc(arr)
    return
  for i in range(N):
    if not visited[i]:
      visited[i] = True
      arr.append(i)
      make_route(arr, count + 1)
      arr.pop()
      visited[i] = False

make_route([], 1)
print(min_total)