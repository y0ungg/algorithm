import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

maximum = -0xfffffff

def do(arr, energy):
  global maximum
  if (len(arr) == 2):
    maximum = max(maximum, energy)
    return
  for i in range(1, len(arr) - 1):
    en = arr[i-1] * arr[i+1]
    temp = arr.pop(i)
    do(arr, energy + en)
    arr.insert(i, temp)
    
do(nums, 0)
print(maximum)