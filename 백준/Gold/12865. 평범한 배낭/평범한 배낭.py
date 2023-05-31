import sys
input = sys.stdin.readline
N, K = map(int, input().split())
weight_and_value = []
for _ in range(N):
  w, v = map(int, input().split())
  weight_and_value.append((w, v))

weight_and_value = sorted(weight_and_value)
max_values = [0 for _ in range(K + 1)]

for i in range(N):
  cur_w, cur_v = weight_and_value[i]
  for j in range(K, cur_w - 1, -1):
    max_values[j] = max(max_values[j], max_values[j - cur_w] + cur_v)
    
print(max_values[K])