import sys
input = sys.stdin.readline
def draw(depth):
  global flag
  if depth == 15:
    for i in range(6):
      for j in range(3):
        if tmp_score[i][j] != score[i][j]: return
    flag = 1
    return
  left, right = board[depth][0], board[depth][1]
  if score[left][0] > 0 and score[right][2] > 0:
    tmp_score[left][0] += 1
    tmp_score[right][2] += 1
    draw(depth + 1)
    tmp_score[left][0] -= 1
    tmp_score[right][2] -= 1
  
  if score[left][1] > 0 and score[right][1] > 0:
    tmp_score[left][1] += 1
    tmp_score[right][1] += 1
    draw(depth + 1)
    tmp_score[left][1] -= 1
    tmp_score[right][1] -= 1
    
  if score[left][2] > 0 and score[right][0] > 0:
    tmp_score[left][2] += 1
    tmp_score[right][0] += 1
    draw(depth + 1)
    tmp_score[left][2] -= 1
    tmp_score[right][0] -= 1
    

result = []
for _ in range(4):
  tmp = list(map(int, input().split()))
  score = []
  for i in range(0, 16, 3):
    w, d, l = tmp[i], tmp[i+1], tmp[i+2]
    score.append([w, d, l])
  flag = 0
  board = []
  for i in range(5):
    for j in range(i + 1, 6):
      board.append([i, j])
  tmp_score = [[0 for _ in range(3)] for _ in range(6)]
  draw(0)
  result.append(1) if flag else result.append(0)
print(*result)
