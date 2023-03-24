import sys
input = sys.stdin.readline
N = int(input())
stack = []
for i in range(N):
  t = int(input())
  if t == 0: stack.pop()
  else: stack.append(t)
print(sum(stack))