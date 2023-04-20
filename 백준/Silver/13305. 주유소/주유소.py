import sys
input = sys.stdin.readline
N = int(input())
distance = list(map(int, input().split()))
pay = list(map(int, input().split()))

total = sum(distance)
init_pay = 0
for i in range(len(distance)):
  init_pay += distance[i] * pay[i]
  
m = 0
for i in range(len(distance)):
  temp = m + (total * pay[i])
  init_pay = min(temp, init_pay)
  total -= distance[i]
  m += distance[i] * pay[i]

print(init_pay)