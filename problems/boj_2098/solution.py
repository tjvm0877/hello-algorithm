import sys

sys.setrecursionlimit(10**7)
input = lambda: sys.stdin.readline().rstrip()
INF = sys.maxsize


def tsp(n, visited, current, adj, dp):
    # 모든 도시 방문: 마지막 도시→시작점(0번) 이동 비용, 이동 불가시 INF
    if visited == (1 << n) - 1:
        return adj[current][0] if adj[current][0] > 0 else INF

    # 이미 계산한 값은 재활용
    if dp[visited][current] != -1:
        return dp[visited][current]

    # 최소 비용 찾기
    ans = INF
    for nxt in range(n):
        # 아직 방문 안했고, 이동 비용이 0이 아닌 도시만
        if not (visited & (1 << nxt)) and adj[current][nxt]:
            cost = tsp(n, visited | (1 << nxt), nxt, adj, dp) + adj[current][nxt]
            ans = min(ans, cost)

    dp[visited][current] = ans
    return ans


if __name__ == "__main__":
    N = int(input())
    adj = []
    dp = [[-1] * N for _ in range(1 << N)]
    for _ in range(N):
        adj.append(list(map(int, input().split())))

    print(tsp(N, 1, 0, adj, dp))
