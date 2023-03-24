N = int(input())

def func(target):
  stack = []
  for x in target:
    if x == '(': stack.append('(')
    elif x == ')' and len(stack) > 0:
      stack.pop()
    else: return "NO"
  if len(stack) == 0: return "YES"
  else: return "NO"
  
for i in range(N):
  T = list(map(str, input()))
  print(func(T))