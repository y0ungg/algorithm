import sys
input = sys.stdin.readline
from math import sqrt

N, M = map(int, input().split())

def check(num):
  if num == 1: return False
  if num <= 3: return True
  cur = int(sqrt(num))
  for i in range(2, cur + 1):
    if num % i == 0: return False
  return True

for i in range(N, M+1):
  check(i)
  if check(i) == True:
    print(i)
  else: continue