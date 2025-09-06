n = int(input())
n_arr = map(int, input().split())

ans = 0
for num in n_arr:
    if num == 1:
        continue

    is_prime_number = True
    for i in range(2, num):
        if num == 1:
            continue

        if num % i == 0:
            is_prime_number = False
            break

    if is_prime_number is True:
        ans += 1

print(ans)
