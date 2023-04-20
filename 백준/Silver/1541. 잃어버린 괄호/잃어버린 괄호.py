import sys
input = sys.stdin.readline
import re
T = list(re.split('([-|+])', input()))
  
temp = 0
minus = []
for i in range(len(T)):
  if T[i] == "-":
    minus.append(temp)
    temp = 0
    continue
  if T[i] == "+":
    continue
  else: temp += int(T[i])

minus.append(temp)
total = minus[0] or 0
for x in range(1, len(minus)):
  total -= minus[x]
print(total)