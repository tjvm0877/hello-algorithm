def is_prime_number(n: int):
    if n == 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True


t = int(input())
for i in range(t):
    n = int(input())
    a = int(n / 2)
    b = int(n / 2)

    while not is_prime_number(a) or not is_prime_number(b):
        a += 1
        b -= 1
    print(f"{b} {a}")
