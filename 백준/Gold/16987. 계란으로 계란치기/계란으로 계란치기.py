import sys
input = sys.stdin.readline
N = int(input())
init_eggs = []
for _ in range(N):
  init_eggs.append(list(map(int, input().split())))
  
big_count = 0
def dfs(depth, eggs):
  global big_count
  if depth == N:
    count = 0
    for sw in eggs:
      if sw[0] <= 0: count += 1
    big_count = max(big_count, count)
    return
  if eggs[depth][0] > 0:
    for i in range(N):
      flag = 0
      if depth == i: continue
      if eggs[i][0] > 0:
        flag = 1
        coiped = [i[:] for i in eggs]
        coiped[depth][0] -= coiped[i][1]
        coiped[i][0] -= coiped[depth][1]
        dfs(depth + 1, coiped)
    if not flag: dfs(depth + 1, eggs)
  else: dfs(depth + 1, eggs)

dfs(0, init_eggs)
print(big_count)
  