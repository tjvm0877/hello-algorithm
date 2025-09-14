import sys

sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip()


def get_longest_increasing_subsequence(i, prev_idx, dp):
    if i == len(arr):
        return 0

    if dp[i][prev_idx] != -1:
        return dp[i][prev_idx]

    # 현재 원소를 선택하지 않는 경우
    not_take = get_longest_increasing_subsequence(i + 1, prev_idx, dp)

    # 현재 원소를 선택하는 경우
    take = 0
    if (
        prev_idx == 0 or arr[i] > arr[prev_idx - 1]
    ):  # prev_idx가 0이면 아직 선택된 원소가 없음
        take = 1 + get_longest_increasing_subsequence(i + 1, i + 1, dp)

    dp[i][prev_idx] = max(not_take, take)
    return dp[i][prev_idx]


n = int(input())
arr = list(map(int, input().split()))
dp = [[-1] * (n + 1) for _ in range(n)]
print(get_longest_increasing_subsequence(0, 0, dp))
