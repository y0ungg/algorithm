import sys
input = sys.stdin.readline

N = int(input())
m = []
for _ in range(N):
  m.append(list(map(int, input().split())))

min_total = 3000
visited = [[0] * N for _ in range(N)]
delta = ((-1, 0), (1, 0), (0, 1), (0, -1))
def make_arr(total, count):
  global min_total, flag
  if count == 4:
    min_total = min(min_total, total)
    return
  for i in range(1, N-1):
    for j in range(1, N-1):
      if not visited[i][j]:
        if all([not visited[i + x][j + y] for x, y in delta]):
          visited[i][j] = 1
          total += m[i][j]
          for x, y in delta:
            visited[i + x][j + y] = 1
            total += m[i + x][j + y]
          make_arr(total, count + 1)
          for x, y in delta:
            visited[i + x][j + y] = 0
            total -= m[i + x][j + y]
          total -= m[i][j]
          visited[i][j] = 0

make_arr(0, 1)
print(min_total)