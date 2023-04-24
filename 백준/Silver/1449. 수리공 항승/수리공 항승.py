import sys 
input = sys.stdin.readline

N, L = map(int, input().split())
l = list(map(int, input().split()))
g = [False] * 1001
for x in l:
  g[x] = True

count = 0
width = 1
for i in range(1001):
  if not g[i] and width > 0:
    width -= 1
  elif g[i] and width == 0:
    width = L - 1
    count += 1
  elif g[i]:
    width -= 1
print(count)