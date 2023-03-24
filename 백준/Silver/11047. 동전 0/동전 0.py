import sys
input = sys.stdin.readline
N, T = map(int, input().split())
l = []
for i in range(N):
  a = int(input())
  if T < a: break
  l.append(a)
   
count = T // l[-1]
num = T % l[-1]

while num > 0:
  fl = list(filter(lambda x: x <= num , l))
  count += num // fl[-1]
  num = num % fl[-1]
print(count)