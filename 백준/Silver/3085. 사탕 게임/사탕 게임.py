import sys
input = sys.stdin.readline
import copy

N = int(input())
matrix = []
for _ in range(N):
  a = list(map(str, input()))
  matrix.append(a)

def check(m):
  total = 1
  for i in range(N):
    x_count = 1
    y_count = 1
    for j in range(1, N):
      if m[i][j] == m[i][j-1]:
        x_count += 1
      if m[i][j] != m[i][j-1]:
        total = max(total, x_count)
        x_count = 1
      if m[j][i] == m[j-1][i]:
        y_count += 1
      elif m[j][i] != m[j-1][i]:
        total = max(total, y_count)
        y_count = 1
    total = max(total, x_count, y_count)
  return total

max_t = 0
def swap(m):
  global max_t
  max_t = max(check(matrix), max_t)
  for i in range(N):
    for j in range(N):
      if j + 1 < N:
        m[i][j], m[i][j+1] = m[i][j+1], m[i][j]
        max_t = max(check(m), max_t)
        m[i][j], m[i][j+1] = m[i][j+1], m[i][j]
      if i + 1 < N:
        m[i][j], m[i+1][j] = m[i+1][j], m[i][j]
        max_t = max(check(m), max_t)
        m[i][j], m[i+1][j] = m[i+1][j], m[i][j]

swap(matrix)
print(max_t)