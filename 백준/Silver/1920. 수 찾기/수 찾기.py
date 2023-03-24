import sys
input = sys.stdin.readline
N = int(input())
l = list((map(int, input().split())))
d = dict(zip(l, l))

M = int(input())
list_M = list(map(int, input().split()))
for num in list_M:
  if d.get(num) == None: print(0)
  else: print(1)