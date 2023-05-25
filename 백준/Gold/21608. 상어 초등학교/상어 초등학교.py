import sys
input = sys.stdin.readline
N = int(input())
students = []
for _ in range(N**2):
  students.append(list(map(int, input().split())))

visited = [0 for _ in range((N**2) + 1)]
visited[students[0][0]] = (1, 1)

delta = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def yes_friend(here, seat_list):
  max_friend_count, max_empty_count = 0, 0
  target = [N-1, N-1]
  for sx, sy in seat_list:
    friend_count, empty_count = 0, 0
    for dx, dy in delta:
      nx, ny = sx + dx, sy + dy
      if 0 <= nx < N and 0 <= ny < N:
        if seats[nx][ny] in here: friend_count += 1
        if not seats[nx][ny]: empty_count += 1
    if max_friend_count < friend_count or (
       max_friend_count == friend_count and max_empty_count < empty_count
    ):
      max_friend_count = friend_count
      max_empty_count = empty_count
      target = [sx, sy]
    elif max_friend_count == friend_count and max_empty_count == empty_count:
      if (sx < target[0]) or (sx == target[0] and sy < target[1]):
        target = [sx, sy]
  return target[0], target[1]

def no_friend():
  max_count = 0
  target = [N, N]
  for sx in range(N):
    for sy in range(N):
      if seats[sx][sy]: continue
      count = 0
      for dx, dy in delta:
        nx, ny = sx + dx, sy + dy
        if 0 <= nx < N and 0 <= ny < N:
          if not seats[nx][ny]: count += 1
      if max_count < count or (sx < target[0] and sy < target[1]):
        max_count = count
        target = [sx, sy]
      if max_count == count:
        if (sx < target[0]) or (sx == target[0] and sy < target[1]):
          target = [sx, sy]
  return target[0], target[1]

def dfs(here):
  person = here[0]
  flag = 0
  seat_list = set()
  for friend in here[1:5]:
    if not visited[friend]: continue
    fx, fy = visited[friend]
    for dx, dy in delta:
      nx, ny = fx + dx, fy + dy
      if 0 <= nx < N and 0 <= ny < N:
        if seats[nx][ny]: continue
        flag = 1
        seat_list.add((nx, ny))
  if flag:
    x, y = yes_friend(here[1:5], sorted(seat_list, reverse=True))
  if not flag:
    x, y = no_friend()
  seats[x][y] = person
  visited[person] = (x, y)

seats = [[0 for _ in range(N)] for _ in range(N)]
seats[1][1] = students[0][0]
for student in students[1:]:
  dfs(student)

total_count = 0
def check(here):
  global total_count
  person, friends = here[0], here[1:5]
  count = 0
  sx, sy = visited[person]
  for dx, dy in delta:
    nx, ny = sx + dx, sy + dy
    if 0 <= nx < N and 0 <= ny < N:
      if seats[nx][ny] in friends: count += 1
  if count == 1: total_count += 1
  if count == 2: total_count += 10
  if count == 3: total_count += 100
  if count == 4: total_count += 1000

for student in students:
  check(student)

print(total_count)