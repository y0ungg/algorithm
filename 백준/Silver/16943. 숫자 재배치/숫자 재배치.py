import sys
input = sys.stdin.readline
A, B = map(str, input().split())
nums = []
for num in A:
  nums.append(int(num))
visited = [0 for _ in range(len(nums))]
max_num = -1
def do(num, arr):
  global max_num
  if num >= int(B):
    return
  if len(arr) == len(A) and arr[0] > 0:
    max_num = max(max_num, num)
  for i in range(len(nums)):
    if visited[i]: continue
    visited[i] = 1
    arr.append(nums[i])
    do((num * 10) + nums[i], arr)
    arr.pop()
    visited[i] = 0

do(0, [])
print(max_num)