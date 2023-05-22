import sys
input = sys.stdin.readline
N = int(input())
nums = []

def make(num):
  nums.append(int(num))
  last_num = int(num[-1])
  for n in range(10):
    if n < last_num:
      num += str(n)
      make(num)
      num = num[:-1]
      
for i in range(10):
  make(str(i))

print(sorted(nums)[N] if len(nums) > N else -1)