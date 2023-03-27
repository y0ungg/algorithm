import sys
input = sys.stdin.readline
T = int(input())
queue = []
for i in range(T):
  s = list(map(str, input().split()))
  if 'push' in s:
    queue.append(s[1])
  if 'pop' in s:
    if len(queue) == 0:
      print(-1)
    else:
      print(queue[0])
      queue.remove(queue[0])
  if 'size' in s:
    print(len(queue))
  if 'empty' in s:
    print(1 if len(queue) == 0 else 0)
  if 'front' in s:
    print(queue[0] if len(queue) > 0 else -1)
  if 'back' in s:
    print(queue[-1] if len(queue) > 0 else -1)