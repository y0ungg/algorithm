import sys
input = sys.stdin.readline

N = int(input())
g = []
for _ in range(N):
  g.append(list(map(int, input().split())))

def do(board):
  copied = [row[:] for row in board]
  count = 0
  for i in range(N):
    for j in range(N):
      copied[i][j] = board[N-1-j][count]
    count += 1
  return copied
 
def go(board):
  result = []
  for row in board:
    temp = []
    for num in row:
      if num > 0: temp.append(num)
    cur1 = len(temp) - 1
    cur2 = len(temp) - 2
    stack = []
    while cur1 >= 0:
      if temp[cur1] != temp[cur2] and cur2 >= 0:
        stack.append(temp[cur1])
        cur1 -= 1
        cur2 -= 1
      if temp[cur1] == temp[cur2] and cur2 >= 0:
        stack.append(temp[cur1] * 2)
        cur1 -= 2
        cur2 -= 2
      if cur1 == 0:
        stack.append(temp[cur1])
        break
    for _ in range(len(row) - len(stack)):
      stack.append(0)
    result.append(stack[::-1])
  return result

max_num = 0
def dfs(board, depth):
  global max_num  
  if depth == 5:
    for row in board:
      for x in row:
        max_num = max(max_num, x)
    return
  for i in range(4):
    tmp = do(board)
    for rad in range(i):
      tmp = do(tmp)
    dfs(go(tmp), depth + 1)
  
dfs([row[:] for row in g], 0)
print(max_num)