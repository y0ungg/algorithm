import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
used = {}
check = [0] * (N+1)

def nohead(arr, depth):
  global used
  if (len(arr) >= M): 
    if str(arr) not in used:
      used[str(arr)] = 1
      print(*arr)
    return
  for i in range(N):
    if not check[i]:
      check[i] = 1
      arr.append(nums[i])
      nohead(arr, depth + 1)
      arr.pop()
      check[i] = 0

nohead([], 1)