import sys
input = sys.stdin.readline
def do(curA, curB):
  arr_A, arr_B = [curA], [curB]
  while parents[curA]:
    arr_A.append(parents[curA])
    curA = parents[curA]
  while parents[curB]:
    arr_B.append(parents[curB])
    curB = parents[curB]
  if len(arr_A) < len(arr_B):
    for cur in arr_A:
      for i in range(len(arr_B)):
        if cur == arr_B[i]:
          print(cur)
          return
  else: 
    for cur in arr_B:
      for i in range(len(arr_A)):
        if cur == arr_A[i]:
          print(cur)
          return

T = int(input())
while T:
  T -= 1
  N = int(input())
  parents = [0 for _ in range(N+1)]
  for _ in range(N-1):
    a, b = map(int, input().split())
    parents[b] = a
  A, B = map(int, input().split())
  do(A, B)