import sys 
input = sys.stdin.readline

N = int(input())
l = list(input().split())

def check(a, b, idx):
  if l[idx] == '<':
    return a < b
  if l[idx] == '>':
    return a > b
  
big = ''
small = ''
visited = [False] * 10
def nums(s, count):
  global small, big
  if count == N + 1:
    if len(small) == 0: small = s
    else: big = s
    return
  for i in range(10):
    if not visited[i]:
      if len(s) > 0:
        if not check(s[-1], str(i), s.index(s[-1])): continue
      visited[i] = True
      s += str(i)
      nums(s, count + 1)
      s = s[:-1]
      visited[i] = False
      
nums('', 0)
print(big)
print(small)