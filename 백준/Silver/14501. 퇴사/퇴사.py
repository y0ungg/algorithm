import sys
input = sys.stdin.readline

times, pays = [], []
N = int(input())
for _ in range(N):
  [time, pay] = map(int, input().split())
  times.append(time)
  pays.append(pay)
  
max_pay = 0

def do(day, total_pay):
  global max_pay
  if day >= N:
    max_pay = max(max_pay, total_pay)
    return
  if day + times[day] <= N:
    do(day + times[day], total_pay + pays[day])
  do(day + 1, total_pay)
  
do(0,0)
print(max_pay)