N = int(input())
l = []

for i in range(N):
  a, b = map(int, input().split())
  l.append([a,b])

result = []
for i in range(N):
  count = 0
  for j in range(N):
    if l[i][0] < l[j][0] and l[i][1] < l[j][1]:
      count = count + 1
  result.append(count + 1)

for idx in result:
  print(idx)