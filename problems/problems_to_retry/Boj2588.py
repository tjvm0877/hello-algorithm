a = int(input())
b = int(input())

# 3의 자리
t = a * (b // 100)
b = b % 100

# 2의 자리
s = a * (b // 10)
b = b % 10

# 1의 자리
f = a * b

print(f)
print(s)
print(t)
print(f + (s * 10) + (t * 100))
