import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
used = {}

def nohead(arr, depth):
  global used
  if (len(arr) >= M): 
    if str(arr) not in used:
      used[str(arr)] = 1
      print(*arr)
    return
  for i in range(N):
    if len(arr) > 0 and nums[i] < arr[-1]: continue
    arr.append(nums[i])
    nohead(arr, depth + 1)
    arr.pop()

nohead([], 1)
