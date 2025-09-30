import sys

input = lambda: sys.stdin.readline().rstrip()
INF = int(1e9)

n = int(input())  # 노드 수
m = int(input())  # 간선 수
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신으로 가는 비용은 0
for a in range(1, n + 1):
    graph[a][a] = 0

# 간선 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, n + 1):  # 경유지
    for a in range(1, n + 1):  # 출발지
        for b in range(1, n + 1):  # 도착지
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
