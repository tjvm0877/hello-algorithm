# DFS 풀이법
import sys

# 재귀 함수 호출 제한을 늘려 깊은 재귀를 허용
sys.setrecursionlimit(10 * 6)


input = lambda: sys.stdin.readline().rstrip()

N = int(input())  # 노드 수 입력

# 1부터 N까지 노드 인덱스에 대응하는 인접 리스트 생성
graph = [[] for _ in range(N + 1)]

# 각 노드의 부모를 저장할 리스트, 0으로 초기화
parent = [-1] * (N + 1)

# 간선 입력 받아 무방향 그래프로 그래프 구성
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


# 재귀 DFS 함수 정의
# node: 현재 방문 노드, p: 부모 노드
def dfs(node, p):
    # 현재 노드와 연결된 인접 노드를 하나씩 확인
    for adj in graph[node]:
        # 부모 노드와 같으면 무한 재귀 방지를 위해 탐색하지 않음
        if adj != p:
            parent[adj] = node  # 인접 노드의 부모를 현재 노드로 설정
            dfs(adj, node)  # 인접 노드로 재귀 호출하여 깊이 우선 탐색 수행


# 1번 노드를 루트로 DFS 시작, 부모 노드 0 지정
dfs(1, 0)

# 2번 노드부터 N번 노드까지 부모 노드 출력
for i in range(2, N + 1):
    print(parent[i])
