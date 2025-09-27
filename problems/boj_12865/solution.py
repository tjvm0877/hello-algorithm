import sys

input = sys.stdin.readline


N, K = map(int, input().split())  # 물건의 개수 N, 가방의 최대 용량 K
stuff = []  # 물건의 무게와 가치를 저장할 리스트
for _ in range(N):
    w, v = map(int, input().split())  # (무게, 가치) 형태로 추가
    stuff.append((w, v))

# 2차원 메모이제이션 테이블 dp[k][i]: 용량 k에서 i번째 물건까지 고려했을 때 최대 가치
# -1로 초기화: 해당 상태가 아직 계산되지 않았음을 의미
# dp = [[-1] * (N + 1) for _ in range(K + 1)]


def knapsack(k, i):
    # 남은 용량이 0이거나, 더 이상 선택할 물건이 없는 경우 최대 가치는 0
    if k == 0 or i == N:
        return 0

    # 이미 계산된 결과가 있다면 해당 값을 반환
    # if dp[k][i] != -1:
    #     return dp[k][i]

    # 현재 물건의 무게와 가치
    weight, value = stuff[i]

    # 현재 물건을 담는 경우의 값 계산
    # 담을 수 있다면 (k - weight >= 0) 해당 물건의 가치를 더하고 다음 물건 탐색
    include = 0
    if k - weight >= 0:
        include = value + knapsack(k - weight, i + 1)

    # 현재 물건을 담지 않는 경우의 값 계산
    exclude = knapsack(k, i + 1)

    # 두 경우 중 더 큰 값을 dp[k][i]에 저장
    # dp[k][i] = max(include, exclude)
    return max(include, exclude)


# 최대 가치 출력 (0번째 물건부터 탐색, 용량 K의 가방)
print(knapsack(K, 0))
