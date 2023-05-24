from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
belt = deque(map(int, input().split()))
robots = deque(0 for _ in range(N))
count = 0
while True:
  robots.rotate(1)
  belt.rotate(1)
  robots[N-1] = 0
  for i in range(N-2, -1, -1):
    if belt[i+1] > 0 and not robots[i+1] and robots[i]:
      robots[i], robots[i+1] = 0, 1
      belt[i+1] -= 1
  robots[N-1] = 0
  if belt[0] > 0 and not robots[0]:
    belt[0] -= 1
    robots[0] = 1
  count += 1
  if belt.count(0) >= K: break
print(count)