import sys
input = sys.stdin.readline

matrix = []
for _ in range(5):
  matrix.append(input().split())

res = set()
a = [0, 0, 1, -1]
b = [1, -1, 0, 0]
def make_arr(i, j, s):
  s += matrix[i][j]
  if len(s) == 6:
    res.add(''.join(s))
    return
  for x in range(4):
    new_i = i + a[x]
    new_j = j + b[x]
    if 0 <= new_i < 5 and 0 <= new_j < 5:
      make_arr(new_i, new_j, s)

for i in range(5):
  for j in range(5):
    make_arr(i, j, '')

print(len(res))