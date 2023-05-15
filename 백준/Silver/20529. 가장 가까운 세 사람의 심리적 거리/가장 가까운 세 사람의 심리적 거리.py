import sys
input = sys.stdin.readline
N = int(input())
for _ in range(N):
  T = int(input())
  l = list(map(str, input().split()))
  count = 13
  if T > 32:
    print(0)
  else:
    for i in range(T-2):
      for j in range(i+1, T-1):
        for k in range(j+1, T):
          temp = 0
          for mbti in range(4):
            if l[i][mbti] != l[j][mbti]: temp += 1
            if l[j][mbti] != l[k][mbti]: temp += 1
            if l[i][mbti] != l[k][mbti]: temp += 1
          count = min(count, temp)
    print(count)