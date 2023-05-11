import sys
input = sys.stdin.readline
S = input().rstrip()
visited = [0 for _ in range(len(S))]
res = set()
def do(s, depth):
  if len(s) == len(S):
    res.add(s)
    return
  for i in range(len(S)):
    if visited[i]: continue
    visited[i] = 1
    if s[-1] != S[i]:
      do(s + S[i], depth + 1)
    visited[i] = 0
    
set_str = set()
for i in range(len(S)):
  if not S[i] in set_str:
    set_str.add(S[i])
    visited[i] = 1
    do(S[i], 1)
    visited[i] = 0
    
print(len(res))