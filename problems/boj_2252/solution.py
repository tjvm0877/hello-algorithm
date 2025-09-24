from collections import deque
import sys


input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]  # 인접 리스트
indegree = [0] * (n + 1)  # 진입차수 배열

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)  # a에서 b로 가는 간선
    indegree[b] += 1  # b의 진입차수 증가


def topology_sort():
    result = []
    queue = deque()

    # 진입차수가 0인 모든 노드를 큐에 삽입
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)

    # 큐가 빌 때까지 반복
    while queue:
        now = queue.popleft()
        result.append(now)

        # 해당 노드와 연결된 간선들을 제거하고
        # 새롭게 진입차수가 0이 된 노드를 큐에 삽입
        for next_node in graph[now]:
            indegree[next_node] -= 1
            if indegree[next_node] == 0:
                queue.append(next_node)
    print(*result)


topology_sort()
