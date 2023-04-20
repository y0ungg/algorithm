import sys
input = sys.stdin.readline
N, M = map(int, input().split())

result = [-1]
def calc(cur, count):
  if cur > M:
    return
  if cur == M:
    if result[0] == -1:
      result[0] = count
    else: result[0] = min(result[0], count)
    return
  calc(cur * 2, count + 1)
  calc(int(str(cur) + "1"), count + 1)
  
calc(N, 1)
print(result[0])