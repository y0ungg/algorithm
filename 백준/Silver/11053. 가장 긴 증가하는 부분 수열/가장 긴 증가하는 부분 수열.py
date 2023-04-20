import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

def check(target, end):
  max_count = 0
  for i in range(end):
    if nums[i] < target:
      max_count = max(max_count, dp[i])
  return max_count

dp = [0] * (N + 1)
dp[0] = 1
for i in range(1, N):
  n = check(nums[i], i)
  if nums[i] == nums[i-1]:
    dp[i] = dp[i-1]
  else:
    dp[i] = n + 1

print(max(dp)) 