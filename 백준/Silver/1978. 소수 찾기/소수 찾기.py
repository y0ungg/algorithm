import math

N = int(input())
arr = list(map(int, input().split()))

nums = [i for i in range(0, 1001)]

count = 0

for i in range(1001):  
    j = 2
    while (j <= math.sqrt(nums[i])):
      if nums[i] % j == 0:
        nums[i] = False
        break
      j += 1

for n in range(N):
  if nums[arr[n]] == 1 or nums[arr[n]] == 0:
    continue
  if nums[arr[n]] != False:
    count += 1

print(count)