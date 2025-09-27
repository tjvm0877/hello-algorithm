import sys


input = lambda: sys.stdin.readline().rstrip()

dp = [-1] * 91
dp[0] = 0
dp[1] = 1


def fibonacci(n):
    if dp[n] != -1:
        return dp[n]

    f = fibonacci(n - 1) + fibonacci(n - 2)
    dp[n] = f

    return f


if __name__ == "__main__":
    N = int(input())
    print(fibonacci(N))
