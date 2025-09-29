import sys


sys.setrecursionlimit(10**8)


def memoization(target, dp=None):
    if target == 0:
        return 1
    elif target < 0:
        return 0

    if not dp:
        dp = [-1] * (target + 1)

    if dp[target] != -1:
        return dp[target]

    # 1을 넣는다.
    one = memoization(target - 1, dp)

    # 00을 넣는다.
    zero = memoization(target - 2, dp)

    # 두 결과를 합친값에 15746으로 나눈 나머지를 리턴
    total_number_of_case = (one + zero) % 15746
    dp[target] = total_number_of_case
    return dp[target]


def tabulation(target):
    if target == 1:
        return 1
    if target == 2:
        return 2
    dp = [0] * (target + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, target + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 15746
    return dp[target]


if __name__ == "__main__":
    N = int(input())
    print(memoization(N))
    print(tabulation(N))
