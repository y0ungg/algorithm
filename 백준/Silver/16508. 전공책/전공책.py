import sys
input = sys.stdin.readline

T = input().rstrip()
N = int(input())
books = []
for _ in range(N):
  a, b = map(str, input().split())
  c = {}
  for x in b:
    if x in c:
      c[x] += 1
    else: c[x] = 1
  books.append([int(a), c])
  
target = {}
for x in T:
  if x in target:
    target[x] += 1
  else: target[x] = 1
    
def name(arr):
  n = {}
  total = 0
  for i in range(len(arr)):
    total += books[arr[i]][0]
    for x in target:
      if x in books[arr[i]][1]:
        if x in n:
          n[x] += books[arr[i]][1][x]
        else: n[x] = books[arr[i]][1][x]
  for t in target:
    if not t in n: return -1
    if target[t] > n[t]: return -1
  return total

res = 1000000000000000000000000
def do(arr, count):
  global res
  if len(arr) <= N:
    if len(arr) > 0:
      a = name(arr)
      if a > 0: res = min(res, a)
  for i in range(N):
    if len(arr) == 0 or arr[-1] < i:
      arr.append(i)
      do(arr, count + 1)
      arr.pop()
      
do([], 1)
print(res if res < 1000000000000000000000000 else -1)