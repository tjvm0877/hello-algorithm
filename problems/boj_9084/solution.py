# 동전이 , 목표가 3원이고 동전이 [1,2] 일 때
# 1원을 사용하지 않은 경우:
#   2원 동전만 사용해서 3원을 맞추는 경우의 수를 구합니다.
#   (실제로 2원 동전만 가지고는 3원을 맞출 수 없으므로 0)
# 1원을 사용한 경우:
#   1원 한 개를 사용한 뒤,
#       남은 2원을 다시 1원/2원 동전으로 맞추는 경우의 수를 구함
#          이 2원을 맞추는 방법은 , 이므로 총 2가지
# 최종 결과: 0 (1원을 사용하지 않은 경우) + 2 (1원을 사용한 경우) = 2가지

import sys

sys.setrecursionlimit(10**8)
input = lambda: sys.stdin.readline().rstrip()


def count_ways_memo(coins, m, coin_index=0, memo=None):
    if memo is None:
        memo = {}

    if m == 0:
        return 1
    if m < 0 or coin_index >= len(coins):
        return 0

    # DP에 값 있는지 확인
    if (m, coin_index) in memo:
        return memo[(m, coin_index)]  # 있으면 리턴

    include = count_ways_memo(coins, m - coins[coin_index], coin_index, memo)
    exclude = count_ways_memo(coins, m, coin_index + 1, memo)

    memo[(m, coin_index)] = include + exclude  # DP에 저장
    return include + exclude


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        coins = list(map(int, input().split()))
        M = int(input())

        result = count_ways_memo(coins, M)
        print(result)
