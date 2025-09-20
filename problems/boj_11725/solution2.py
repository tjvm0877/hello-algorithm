# BFS 풀이법

from collections import deque
import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())  # 노드(정점)의 개수
graph = [[] for _ in range(N + 1)]  # 인접 리스트 방식의 그래프 표현 (1번 노드부터 사용)

# 각 노드의 부모를 저장할 리스트
# -1로 초기화해야 BFS에서 방문 여부를 판별할 수 있음
parent = [-1] * (N + 1)

# 트리의 간선 정보를 입력 받아 양방향 그래프로 저장
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs():
    queue = deque()
    queue.append(1)  # 루트 노드(1번 노드)부터 탐색 시작
    parent[1] = 0  # 루트 노드의 부모를 0으로 설정 (실제 부모 없음)

    # BFS 탐색
    while queue:
        p = queue.popleft()
        # 현재 노드 p와 연결된 인접 노드 탐색
        for adj in graph[p]:
            # 이미 부모가 지정된 노드는 방문한 적이 있으므로 스킵
            if parent[adj] != -1:
                continue
            # 방문하지 않았다면 현재 노드 p를 부모로 설정
            parent[adj] = p
            queue.append(adj)


# BFS 수행하여 모든 노드의 부모 찾기
bfs()

# 루트(1번 노드)를 제외한 2번 노드부터 N번 노드까지의 부모 출력
for i in range(2, N + 1):
    print(parent[i])
