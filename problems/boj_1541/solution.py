import sys


input = lambda: sys.stdin.readline().rstrip()


expression = input().split("-")
ans = 0
for i in range(len(expression)):
    exp = expression[i].split("+")
    sum = 0
    for num in exp:
        sum += int(num)

    if i == 0:
        ans += sum
    else:
        ans -= sum
print(ans)
