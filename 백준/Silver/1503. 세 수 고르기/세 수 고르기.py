import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = [0 for _ in range(1002)]
if M:
  s = list(map(int, input().split()))
  for i in range(M):
    nums[s[i]] = 1

min_num = 0xffffff
for x in range(1, 1002):
  if nums[x]: continue
  for y in range(x, 1002):
    if nums[y]: continue
    for z in range(y, 1002):
      if nums[z]: continue
      min_num = min(min_num, abs(N - (x * y * z)))
      if abs(N - (x * y * z)) > N + 1: break
    if not min_num: break
  if not min_num: break
      
print(min_num)