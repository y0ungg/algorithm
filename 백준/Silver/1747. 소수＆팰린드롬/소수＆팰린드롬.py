import sys
input = sys.stdin.readline

N = int(input())
nums = [1 for _ in range(1003002)]
nums[1] = 0

for i in range(2, 1001):
  j = 2
  while i * j < 1003002:
    nums[i * j] = 0
    j += 1
  
for i in range(N, 1003002):
  if nums[i]:
    num = str(i)
    if num == num[::-1]:
      print(int(num))
      break