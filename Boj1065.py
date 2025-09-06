def is_arithmetic(num: int) -> bool:
    if num < 100:
        return True

    str_num = str(num)
    common_diff = 0
    for i in range(1, len(str_num)):
        diff = int(str_num[i]) - int(str_num[i - 1])
        if i == 1:
            common_diff = diff
        if diff != common_diff:
            return False

    return True


n = int(input())

ans = 0
for i in range(1, n + 1):
    if is_arithmetic(i) is True:
        ans += 1
print(ans)
