import sys
input = sys.stdin.readline
S = str(input().rstrip())
if S == S[::-1]:
  print(len(S))
else:
  end = len(S) - 1
  res = 101
  while end > -1:
    target = S
    for i in range(end, -1, -1):
      target += S[i]
    if target == target[::-1]:
      res = min(res, len(target))
    end -= 1
  print(res)