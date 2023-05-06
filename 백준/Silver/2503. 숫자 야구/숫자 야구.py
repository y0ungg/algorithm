import sys
input = sys.stdin.readline
N = int(input())
balls = []
for _ in range(N):
  a, b, c = map(int, input().split())
  balls.append((str(a), b, c))

nums = []
visited = [0] * 10
def make_nums(s):
  if len(s) == 3:
    nums.append(s)
    return
  for i in range(1, 10):
    if not visited[i]:
      visited[i] = 1
      s += str(i)
      make_nums(s)
      s = s[:-1]
      visited[i] = 0
make_nums("")
res = {}
count = 0
for i in range(len(nums)):
  for x in range(N):
    target, strike, ball = balls[x]
    c_strike = 0
    c_ball = 0
    for j in range(3):
      if nums[i][j] == target[j]:
        c_strike += 1
      elif j == 0 and (nums[i][j] == target[1] or nums[i][j] == target[2]):
        c_ball += 1
      elif j == 1 and (nums[i][j] == target[0] or nums[i][j] == target[2]):
        c_ball += 1
      elif j == 2 and (nums[i][j] == target[0] or nums[i][j] == target[1]):
        c_ball += 1
    if c_strike == strike and c_ball == ball:
      if nums[i] in res:
        res[nums[i]] += 1
      else: res[nums[i]] = 1
      if res[nums[i]] == N:
        count += 1   
print(count)