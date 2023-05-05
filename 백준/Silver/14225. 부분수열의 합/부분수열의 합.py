import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
check = [0] * 2000001

def make_nums(s, idx):
  global check
  check[s] = 1
  for i in range(N):
    if s == 0 or idx < i:
      s += nums[i]
      make_nums(s, i)
      s -= nums[i]
      
make_nums(0, -1)

for i in range(len(check)):
  if not check[i]:
    print(i)
    break