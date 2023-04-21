import sys
input = sys.stdin.readline

N, T = map(int, input().split())
nums = list(map(int, input().split()))

total = 0
def do(arr, start):
  global total
  if start == N:
    return
  for i in range(start, N):
    arr.append(nums[i])
    if sum(arr) == T:
      total += 1
    do(arr, i+1)
    arr.pop()

do([], 0)
print(total)