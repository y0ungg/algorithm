import sys
input = sys.stdin.readline
l = [0, 1, 2, 4]
def check(num):
  if len(l) <= num:
    while len(l) <= num:
      count = 0
      i = len(l)
      count = l[i-1] + l[i-2] + l[-3] 
      l.append(count)
  return l[num]
        
        
N = int(input())
for i in range(N):
  T = int(input())
  print(check(T))