import sys
input = sys.stdin.readline
T = int(input())
N = int(input())
if N:
  M = list(map(int, input().split()))
else: M = []

min_num = abs(100 - T)

for num in range(1000001):
  channel = str(num)
  flag = 0
  for n in channel:
    if int(n) in M:
      flag = 1
      break
  if not flag:
    min_num = min(min_num, abs(num - T) + len(channel))

print(min_num)