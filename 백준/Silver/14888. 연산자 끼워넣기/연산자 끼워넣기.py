import sys 
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
P, M, X, Y = map(int, input().split())
l = ['+'] * P + ['-'] * M + ['*'] * X + ['/'] * Y

min_ans = 10000000000
max_ans = -10000000000
def calc(arr):
  global min_ans, max_ans
  ans = nums[0]
  for i in range(1, N):
    if arr[i-1] == '*':
      ans *= nums[i]
    elif arr[i-1] == '-':
      ans -= nums[i]
    elif arr[i-1] == '+':
      ans += nums[i]
    elif arr[i-1] == '/':
      if ans < 0:
        ans = (-ans // nums[i]) * -1
      else: ans //= nums[i]
  min_ans = min(min_ans, ans)
  max_ans = max(max_ans, ans)
  
visited = [False] * (N+1)
def do(arr, count):
  if count == N:
    calc(arr)
    return
  for i in range(N-1):
    if not visited[i]:
      visited[i] = True
      arr.append(l[i])
      do(arr, count + 1)
      arr.pop()
      visited[i] = False
    
do([], 1)
print(max_ans)
print(min_ans)