import sys

sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
is_inside = input()
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    u1, u2 = map(int, input().split())
    graph[u1].append(u2)
    graph[u2].append(u1)

visited = [False] * (N + 1)
total_routes = 0

# 1. 실내끼리 직접 연결된 경우 계산
for i in range(1, N + 1):
    if is_inside[i - 1] == "1":  # 실내인 경우
        for neighbor in graph[i]:
            if is_inside[neighbor - 1] == "1":  # 인접한 곳도 실내
                total_routes += 1  # 양방향이므로 각각 카운트


# 2. 실외 노드를 기준으로 연결된 실내 노드 개수 계산
def dfs(node):
    visited[node] = True
    indoor_count = 0

    for neighbor in graph[node]:
        if is_inside[neighbor - 1] == "1":  # 실내 노드
            indoor_count += 1
        elif not visited[neighbor]:  # 실외 노드이고 미방문
            indoor_count += dfs(neighbor)

    return indoor_count


# 모든 실외 노드에 대해 DFS 수행
for i in range(1, N + 1):
    if is_inside[i - 1] == "0" and not visited[i]:  # 실외이고 미방문
        indoor_count = dfs(i)
        # n개의 실내가 연결되어 있으면 n*(n-1)개의 경로
        total_routes += indoor_count * (indoor_count - 1)

print(total_routes)
