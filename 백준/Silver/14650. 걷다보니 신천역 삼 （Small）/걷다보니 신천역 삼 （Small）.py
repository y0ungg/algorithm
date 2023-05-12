import sys
input = sys.stdin.readline

N = int(input())
res = set()
def do(num, depth, arr):
  if len(arr) == N and arr[0] != 0:
    if num % 3 == 0:
      res.add(num)
    return
  if depth == N:
    return
  for n in [0, 1, 2]:
    arr.append(n)
    do((num * 10) + n, depth + 1, arr)
    arr.pop()
    
do(0, 0, [])
print(len(res))