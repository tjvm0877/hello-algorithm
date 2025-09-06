a, b = map(int, input().split())
reversed_a = int(str(a)[::-1])
reversed_b = int(str(b)[::-1])
print(max(reversed_a, reversed_b))
