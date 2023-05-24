import sys
input = sys.stdin.readline
def check(depth, todo):
  global end
  if depth == end:
    todo += str(depth)
    temp = todo.replace(" ","")
    if not eval(temp): 
      result.append(todo)
    return
  for cur in ["+", "-", " "]:
    todo += str(depth)
    todo += cur
    check(depth + 1, todo)
    todo = todo[:-2]
    
N = int(input())
for _ in range(N):
  end = int(input())
  result = []
  check(1, "")
  print(*sorted(result), sep="\n")
  print()