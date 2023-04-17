import sys
input = sys.stdin.readline

N = int(input())
stairs = [0]
for _ in range(N):
  stairs.append(int(input()))

dp = [0] * (N+1)
if N >= 1:
  dp[1] = stairs[1]
if N >= 2:
  dp[2] = stairs[1] + stairs[2]
if N >= 3:
  dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

for i in range(4, N+1):
  dp[i] = max(dp[i-3]+ stairs[i-1] + stairs[i], dp[i-2] + stairs[i])

print(dp[N])