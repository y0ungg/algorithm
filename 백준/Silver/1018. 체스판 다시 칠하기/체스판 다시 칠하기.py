import sys
input = sys.stdin.readline
H, W = map(int, input().split())
matrix = []
for i in range(H):
  temp = list(map(str, input()))
  matrix.append(temp)

result = []
l1 = [['B','W','B','W','B','W','B','W'],
      ['W','B','W','B','W','B','W','B'],
      ['B','W','B','W','B','W','B','W'],
      ['W','B','W','B','W','B','W','B'],
      ['B','W','B','W','B','W','B','W'],
      ['W','B','W','B','W','B','W','B'],
      ['B','W','B','W','B','W','B','W'],
      ['W','B','W','B','W','B','W','B']]
l2 = [['W','B','W','B','W','B','W','B'],
      ['B','W','B','W','B','W','B','W'],
      ['W','B','W','B','W','B','W','B'],
      ['B','W','B','W','B','W','B','W'],
      ['W','B','W','B','W','B','W','B'],
      ['B','W','B','W','B','W','B','W'],
      ['W','B','W','B','W','B','W','B'],
      ['B','W','B','W','B','W','B','W']]
def check(arg):
  count1 = 0
  count2 = 0
  for i in range(8):
    for j in range(8):
      if arg[i][j] != l1[i][j]:
        count1 += 1
      if arg[i][j] != l2[i][j]:
        count2 += 1
  result.append(count1)
  result.append(count2)
  
for i in range(H-7):
  for j in range(W-7):
    s = [row[j:j+8] for row in matrix[i:i+8]]
    check(s)
print(min(result))