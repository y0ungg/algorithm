import sys
input = sys.stdin.readline
A, B = map(int, input().split())
l = []
def do(num, depth):
  if A <= num <= B:
    l.append(num)
  if num >= B:
    return
  num *= 10
  do(num + 4, depth + 1)
  do(num + 7, depth + 1)

do(0, 0)
print(len(l))