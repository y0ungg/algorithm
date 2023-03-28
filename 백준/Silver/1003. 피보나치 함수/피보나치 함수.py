import sys
input = sys.stdin.readline
l = [[1,0],[0,1]]
def calc(num):
  while num >= len(l):
    i = len(l)
    a = [l[i-1][0] + l[i-2][0], l[i-1][1] + l[i-2][1]]
    l.append(a)
  return l[num]

N = int(input())
for i in range(N):
  t = int(input())
  result = calc(t)
  print(result[0], result[1])