a = list(map(str, input()))
s = sorted(a, reverse=True)
print(int(''.join(s)))