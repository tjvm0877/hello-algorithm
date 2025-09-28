import sys

sys.setrecursionlimit(10**8)
input = lambda: sys.stdin.readline().rstrip()


def find_lcs(i, j, str_x, str_y, dp=None):
    if not dp:
        dp = [[-1 for _ in range(len(str_y))] for _ in range(len(str_x))]

    if i >= len(str_x) or j >= len(str_y):
        return 0

    if dp[i][j] != -1:
        return dp[i][j]

    if str_x[i] == str_y[j]:
        dp[i][j] = 1 + find_lcs(i + 1, j + 1, str_x, str_y, dp)
    else:
        dp[i][j] = max(
            find_lcs(i + 1, j, str_x, str_y, dp),
            find_lcs(i, j + 1, str_x, str_y, dp),
        )

    return dp[i][j]


def lcs_dp(str_x, str_y):
    m, n = len(str_x), len(str_y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m):
        for j in range(n):
            if str_x[i] == str_y[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
    return dp[m][n]


if __name__ == "__main__":
    str_x = list(input())
    str_y = list(input())

    # ans = find_lcs(0, 0, str_x, str_y)
    ans = lcs_dp(str_x, str_y)
    print(ans)
