import sys


input = lambda: sys.stdin.readline().rstrip()


def is_prime_number(n: int) -> bool:
    if n == 1 or 0:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


def get_goldbach_partition(n: int) -> list:
    a = n // 2
    b = n - a

    while not (is_prime_number(a) and is_prime_number(b)):
        a -= 1
        b += 1
    return [a, b]


if __name__ == "__main__":
    n = int(input())

    for _ in range(n):
        num = int(input())
        ans = get_goldbach_partition(num)
        print(f"{ans[0]} {ans[1]}")
