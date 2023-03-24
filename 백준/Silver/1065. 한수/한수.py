N = int(input())
if N < 100:
  print(N)
else:
  count = 99
  for i in range(100, N + 1):
    num_list = list(map(int, str(i)))
    if num_list[0] - num_list[1] == num_list[1] - num_list[2]:
      count += 1
  print(count)