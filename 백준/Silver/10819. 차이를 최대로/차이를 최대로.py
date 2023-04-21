import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

max_total = 0
def calc(arr):
  global max_total
  total = 0
  for i in range(1, N):
    total += abs(nums[arr[i-1]] - nums[arr[i]])
  max_total = max(max_total, total)


def make_arr(arr, count):
  if count == N + 1:
    calc(arr)
    return
  for i in range(N):
    if not i in arr:
      arr.append(i)
      make_arr(arr, count + 1)
      arr.pop()

make_arr([], 1)
print(max_total)