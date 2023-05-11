import sys
input = sys.stdin.readline

N, K = map(int, input().split())
res = []
def check(arr, s):
  if s == N:
    res.append(arr)
    return
  if s > N or len(res) >= K:
    return
  for num in [1, 2, 3]:
    check(arr + [num], s + num)
    
check([], 0)
if len(res) >= K: print("+".join(map(str, res[K-1])))
else: print(-1)