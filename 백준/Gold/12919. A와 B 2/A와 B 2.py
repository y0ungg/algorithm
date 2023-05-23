import sys
input = sys.stdin.readline
S = input().strip()
T = input().strip()

flag = 0
def dfs(string):
  global flag
  if len(string) == len(S):
    if string == S:
      flag = 1
      print(1)
    return
  if string[-1] == "A" and string[0] == "B" and not flag:
    dfs(string[:-1])
    dfs(string[::-1][:-1])
  elif string[-1] == "A" and string[0] == "A" and not flag:
    dfs(string[:-1])
  elif string[-1] == "B" and string[0] == "B" and not flag:
    dfs(string[::-1][:-1])

dfs(T)
if not flag: print(0)