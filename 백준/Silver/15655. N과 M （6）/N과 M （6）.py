import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
used = []

def nohead(arr, depth):
  global used
  if (len(arr) >= M): 
    print(*arr)
    return
  for num in nums:
    if len(arr) > 0 and num < arr[-1]: continue
    if not num in used:
      used.append(num)
      arr.append(num)
      nohead(arr, depth + 1)
      arr.pop()
      used.pop()

nohead([], 1)