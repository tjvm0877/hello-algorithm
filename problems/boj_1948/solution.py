from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

# 그래프와 진입차수 초기화
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
result = [0] * (n + 1)  # 각 노드까지의 최장거리
parent = [[] for _ in range(n + 1)]  # 부모 노드들 저장

# 그래프 구성
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    indegree[b] += 1

start, end = map(int, input().split())

# 1단계: 위상정렬로 최장거리 계산
queue = deque([start])
result[start] = 0

while queue:
    now = queue.popleft()

    for next_node, time in graph[now]:
        # 더 긴 시간으로 갱신되는 경우
        if result[next_node] < result[now] + time:
            result[next_node] = result[now] + time
            parent[next_node] = [now]  # 부모 리스트 초기화
        # 같은 시간인 경우 (여러 최장경로)
        elif result[next_node] == result[now] + time:
            parent[next_node].append(now)  # 부모 추가

        indegree[next_node] -= 1
        if indegree[next_node] == 0:
            queue.append(next_node)

# 2단계: 역추적으로 임계경로 간선 개수 세기
visited = [False] * (n + 1)
edge_count = 0
queue = deque([end])
visited[end] = True

while queue:
    now = queue.popleft()

    for p in parent[now]:
        edge_count += 1  # 간선 개수 증가
        if not visited[p]:
            visited[p] = True
            queue.append(p)

print(result[end])  # 최장시간
print(edge_count)  # 임계경로 간선 개수
