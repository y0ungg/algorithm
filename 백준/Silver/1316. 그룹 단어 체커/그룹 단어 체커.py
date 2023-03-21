N = int(input())
result = 0

def check(word):
  arr = {}
  num = 0
  for char in word:
    if char in arr and arr[char] != num - 1:
      return False
    if char in arr and arr[char] == num - 1:
      arr[char] = num
    if not char in arr:
      arr[char] = num
    num += 1

  return True

for i in range(N): 
  word = input()
  if check(word):
    result += 1
    
  
print(result)