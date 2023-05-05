import sys
input = sys.stdin.readline

N = int(input())
health = list(map(int, input().split()))
joy = list(map(int, input().split()))

total = 0

def go(remaining_health, current_joy, depth):
  global total
  if remaining_health <= 0:
    return
  if depth == N:
    total = max(total, current_joy)
    return
  go(remaining_health - health[depth], current_joy + joy[depth], depth + 1)
  go(remaining_health, current_joy, depth + 1)

go(100, 0, 0)
print(total)