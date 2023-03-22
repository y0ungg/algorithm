N = int(input())

line = 0
carry = 1
s = 0
while N > s:
  line = line + 1
  s = s + carry
  carry = carry + 1


first = s - line + 1
idx = N - first

if line % 2 == 0:
  print(f"{idx + 1}/{line - idx}")
else:
  print(f"{line - idx}/{idx + 1}")