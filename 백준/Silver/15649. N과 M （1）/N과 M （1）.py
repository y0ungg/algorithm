import sys
input = sys.stdin.readline

N, M = map(int, input().split())

used = [0] * (N + 1)  
used[0] = 1

def nohead(arr, depth):
  global used
  if (len(arr) >= M): 
    print(*arr)
    return
  for i in range(1, N+1):
    if not used[i]:
      used[i] = '🤣'
      arr.append(i)
      nohead(arr, depth + 1)
      arr.pop()
      used[i] = 0

nohead([], 1)
  