max = 0
maxloc = 0

for i in range(1, 10):
    num = int(input())
    if num > max:
        max = num
        maxloc = i

print(max)
print(maxloc)
