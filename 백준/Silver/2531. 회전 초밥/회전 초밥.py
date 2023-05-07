import sys
input = sys.stdin.readline

N, D, K ,C = map(int, input().split())
plates = [0 for _ in range(N)]
for i in range(N):
  plates[i] = int(input())

res = 0
start, end = 0, K
while start < N:
  cur = set()
  for i in range(start, end):
    i %= N
    cur.add(plates[i])
  count = len(cur)
  if not C in cur:
    res = max(res, count + 1)
  else: res = max(res, count)
  start += 1
  end = start + K
print(res)