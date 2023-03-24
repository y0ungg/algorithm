import sys
input = sys.stdin.readline
N = int(input())

l = []
for i in range(N):
  T = input()
  if "push" in T:
    s = T.split()
    l.append(int(s[1]))
  if "pop" in T:
    if len(l) == 0: print(-1)
    else: print(l.pop())
  if "size" in T:
    print(len(l))
  if "empty" in T:
    if len(l) == 0: print(1)
    else: print(0)
  if "top" in T:
    if len(l) == 0: print(-1)
    else: print(l[-1])