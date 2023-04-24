import sys 
input = sys.stdin.readline

N = int(input())
visited = [False] * (N + 1)
def do(arr, count):
  if count == N + 1:
    print(*arr)
    return
  for i in range(1, N+1):
    if not visited[i]:
      visited[i]= True
      arr.append(i)
      do(arr, count + 1)
      arr.pop()
      visited[i] = False
do([], 1)