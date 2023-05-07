import sys
input = sys.stdin.readline

D, K = map(int, input().split())

ans = True
def do(one, two, depth):
  global ans
  if one < 1 or two <= one:
    return
  if depth == 2:
    ans = False
    print(one)
    print(two)
    return
  if ans: do(two - one, one, depth - 1)

for i in range(K-1, 2, -1):
  if not ans: break
  do(i, K, D)