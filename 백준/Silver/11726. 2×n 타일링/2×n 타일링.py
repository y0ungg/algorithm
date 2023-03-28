import sys
input = sys.stdin.readline
N = int(input())
l = [0, 1, 2, 3]

def calc(num):
  for i in range(4, num+1):
    s = l[i-1] + l[i-2]
    s = s if s < 10007 else s % 10007
    l.append(s)
  return l[num]

print(calc(N))