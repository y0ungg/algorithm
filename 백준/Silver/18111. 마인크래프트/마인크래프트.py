import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
init_l = []
for _ in range(N):
  s = list(map(int, input().split()))
  for i in range(M):
    init_l.append(s[i])

total = sum(init_l)
min_count, max_node = 999999999999999, 0
min_h, max_h = min(init_l), max(init_l)
for i in range(min_h, max_h + 1):
  if total + B >= i * N * M:
    cur_count = 0
    for h in init_l:
      if h < i:
        cur_count += i - h
      elif h > i:
        cur_count += (h - i) * 2
    if cur_count <= min_count:
      min_count = cur_count
      max_node = i
    
print(min_count, max_node)