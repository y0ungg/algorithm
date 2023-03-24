import sys
input = sys.stdin.readline
N = int(input())
l = sorted((list(map(int, input().split()))))
r = 0
for i in range(N):
  r = r + sum(l[:i+1])
print(r)