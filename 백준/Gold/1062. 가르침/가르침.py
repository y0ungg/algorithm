import sys
input = sys.stdin.readline
N, K = map(int, input().split())
words = []
total = [0 for _ in range(27)]
for x in "antic":
  total[ord(x) - 97] = 1
  
for _ in range(N):
  tmp = input().strip()
  visited = [0 for _ in range(27)]
  for w in tmp:
    t = ord(w) - 97
    if not visited[t]:
      visited[t] = 1
  words.append(visited)
  
count = 0
def select_word(depth, idx):
  global count
  if depth == K - 5:
    tmp = 0
    for word in words:
      flag = 0
      for i in range(27):
        if not word[i]: continue
        if not total[i]:
          flag = 1
          break
      if not flag: tmp += 1
    count = max(count, tmp)
    return
  for i in range(idx, 26):
    if total[i]: continue
    total[i] = 1
    select_word(depth + 1, i + 1)
    total[i] = 0
      
select_word(0, 0)
print(count)