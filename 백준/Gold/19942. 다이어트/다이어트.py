import sys
input = sys.stdin.readline
N = int(input())
MP, MF, MS, MV = map(int, input().strip().split())
food = []
for _ in range(N):
  food.append(tuple(map(int, input().strip().split())))

result = []
min_money = 1000000
def calc(arr):
  global min_money, result, MP, MF, MS, MV
  total = [0, 0, 0, 0, 0]
  for num in arr:
    for i in range(5):
      total[i] += food[num][i]
  if total[0] >= MP and total[1] >= MF and total[2] >= MS and total[3] >= MV:
    min_money = min(min_money, total[4])
    if min_money == total[4]:
      temp = [x + 1 for x in arr]
      if not len(result): result = temp
      else: result = temp if temp < result else result
  return

def cook(arr, depth):
  if depth == N:
    calc(arr)
    return
  cook(arr, depth + 1)
  arr.append(depth)
  cook(arr, depth + 1)
  arr.pop()

cook([], 0)
if len(result):
  print(min_money)
  print(*result)
else: print(-1)