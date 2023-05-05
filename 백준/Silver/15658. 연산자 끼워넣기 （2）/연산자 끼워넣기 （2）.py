import sys
input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
a, b, c, d = map(int, input().split())
if a >= N: a = N-1
if b >= N: b = N-1
if c >= N: c = N-1
if d >= N: d = N-1
big = -1000000000
small = 1000000000
def make_calc(s, depth, n):
  a,b,c,d = n
  global big, small
  if depth == N:
    big = max(big, s)
    small = min(small, s)
    return
  if a > 0:
    make_calc(s + nums[depth], depth + 1, (a-1, b, c, d))
  if b > 0:
    make_calc(s - nums[depth], depth + 1, (a, b-1, c, d))
  if c > 0:
    make_calc(s * nums[depth], depth + 1, (a, b, c-1, d))
  if d > 0:
    if s < 0:
      make_calc(((s * -1) // nums[depth]) * -1, depth + 1, (a, b, c, d-1))
    else:
      make_calc(s // nums[depth], depth + 1, (a, b, c, d-1))
        
make_calc(nums[0], 1, (a,b,c,d))
print(big)
print(small)