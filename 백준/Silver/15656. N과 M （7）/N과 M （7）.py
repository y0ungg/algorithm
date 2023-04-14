import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

def nohead(arr, depth):
  if (len(arr) >= M): 
    print(*arr)
    return
  for num in nums:
    arr.append(num)
    nohead(arr, depth + 1)
    arr.pop()

nohead([], 1)
      