import sys
input = sys.stdin.readline

N = int(input())

min_count = 4
def check(target, count):
  global min_count
  if target == 0:
    min_count = min(min_count, count)
    return
  for i in range(int(target**0.5), int((target//(4-count))**0.5), -1):
    check(target - (i**2), count + 1)
  
check(N, 0)
print(min_count)