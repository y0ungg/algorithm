import sys
input = sys.stdin.readline
L, C = map(int, input().split())
string = sorted(list(input().strip().split()))
flag = "aeiou"

def bfs(s, idx, count):
  if len(s) == L:
    if count >= 1 and L - count >= 2: print(s)
    return
  for i in range(C):
    if len(s) == 0 or idx < i:
      s += string[i]
      tmp = count
      if string[i] in flag: count += 1
      bfs(s, i, count)
      count = tmp
      s = s[:-1]

bfs("", -1, 0)