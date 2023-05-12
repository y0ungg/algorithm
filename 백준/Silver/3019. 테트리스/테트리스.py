import sys
input = sys.stdin.readline
C, P = map(int, input().split())
nums = list(map(int, input().split()))
dic = {
  1: [[0, 0, 0]],
  2: [[0]],
  3: [[0, 1], [-1]],
  4: [[1], [-1, 0]],
  5: [[0, 0], [1], [-1], [-1, 1]],
  6: [[0, 0], [0], [1, 0], [-2]],
  7: [[0, 0], [0], [0, -1], [2]]
}
target = dic[P]
gap_list = []
for i in range(1, C):
  gap_list.append(nums[i] - nums[i-1])      

count = 0
def check():
  global count
  for arr in target:
    t = len(arr)
    for i in range(C-1):
      if gap_list[i:i+t] == arr:
        count += 1

check()
print(count if P > 1 else count + C)