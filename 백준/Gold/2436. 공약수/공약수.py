import sys
input = sys.stdin.readline
N, M = map(int, input().split())
def check(num1, num2):
  a, b = num1, num2
  while a % b:
    temp = a % b
    a = b
    b = temp
  if b != N: return 0
  if (num1 * num2) // N != M: return 0
  return 1
  
target = N * M
arr = []
for i in range(1, (M // N) + 1):
  l = N * i
  r = target // l
  if l > r: break
  flag = check(l, r)
  if flag: arr.append((l, r, l+r))

res = sorted(arr, key=lambda x: x[2])[0]
print(res[0], res[1])