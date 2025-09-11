import sys


input = lambda: sys.stdin.readline().rstrip()


def count_combination(n, total):

    if total > n:
        return 0

    if total == n:
        return 1

    combintation = 0
    for i in range(1, 4):
        combintation += count_combination(n, total + i)

    return combintation


T = int(input())
for _ in range(T):
    n = int(input())
    print(count_combination(n, 0))
