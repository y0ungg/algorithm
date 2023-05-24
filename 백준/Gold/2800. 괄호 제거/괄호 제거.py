import sys
input = sys.stdin.readline
T = list(input().strip())
p = []
stack = []
for i in range(len(T)):
  if T[i] == "(":
    stack.append(i)
  if T[i] == ")":
    p.append((stack.pop(), i))

ans = set()
def dfs(s, depth):
  if depth == len(p):
    ans.add("".join(s))
    return
  l, r = p[depth]
  dfs(s, depth + 1)
  s[l], s[r] = "", ""
  dfs(s, depth + 1)
  s[l], s[r] = "(", ")"

dfs(T, 0)
if "".join(T) in ans:
  ans.remove("".join(T))
print(*sorted(ans), sep="\n")