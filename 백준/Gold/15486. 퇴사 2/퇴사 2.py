import sys
input = sys.stdin.readline
N = int(input())
day = []
money = []
for _ in range(N):
  d, m = map(int, input().split())
  day.append(d)
  money.append(m)

max_money = [0 for _ in range(N + 1)]
for i in range(N-1, -1, -1):
  if i + day[i] > N:
    max_money[i] = max_money[i + 1]
  elif day[i] + i - 1 < i + 1:
    max_money[i] = max_money[i+1] + money[i]
  else:
    max_money[i] = max(max_money[i+1],  max_money[i+day[i]] + money[i])
    
print(max_money[0])