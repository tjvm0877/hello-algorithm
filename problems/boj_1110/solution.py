import sys


input = lambda: sys.stdin.readline().rstrip()


def cycle(N, n, count):

    if count != 0 and n == N:
        return count

    a, b = n // 10, n % 10
    new_number = (b * 10) + ((a + b) % 10)

    return cycle(N, new_number, count + 1)


N = int(input())
print(cycle(N, N, 0))
