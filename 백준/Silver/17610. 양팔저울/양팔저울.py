import sys
input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().strip().split()))
result = [0 for _ in range(sum(nums) + 1)]

target = []
def make_part(cur, else_arr, depth):
  global target
  if depth == len(else_arr):
    target.append(cur)
    return cur
  make_part(cur, else_arr, depth + 1)
  make_part(cur + else_arr[depth], else_arr, depth + 1)

def check(arr):
  global target
  sum_arr = 0
  else_arr = []
  for i in range(N):
    if arr[i]: sum_arr += nums[i]
    else: else_arr.append(nums[i])
  result[sum_arr] = 1
  target = []
  make_part(0, else_arr, 0)
  for num in target:
    result[abs(num - sum_arr)] = 1
  return

def make_arr(arr, depth):
  if depth == N:
    check(arr)
    return
  make_arr(arr, depth + 1)
  arr[depth] = 1
  make_arr(arr, depth + 1)
  arr[depth] = 0

make_arr([0 for _ in range(N)], 0)
print(sum(nums) - (sum(result) - 1))