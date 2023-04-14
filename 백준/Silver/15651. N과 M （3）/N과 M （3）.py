import sys
input = sys.stdin.readline

N, M = map(int, input().split())

def nohead(arr, depth):
  if (len(arr) >= M): 
    print(*arr)
    return
  for i in range(1, N+1):
    arr.append(i)
    nohead(arr, depth + 1)
    arr.pop()

nohead([], 1)