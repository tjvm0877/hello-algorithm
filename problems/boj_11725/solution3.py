# BFS 풀이법 stack 사용

import sys

sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
graph = [[] for _ in range(N + 1)]

# 부모 노드 정보를 저장하는 리스트. 방문 여부도 함께 판별 가능하도록 -1로 초기화
parent = [-1] * (N + 1)

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs_stack(start):
    stack = [start]
    parent[start] = 0  # 루트 노드의 부모는 0으로 설정

    while stack:
        node = stack.pop()
        # node와 인접한 모든 노드 확인
        for adj in graph[node]:
            # 방문하지 않은 노드일 경우
            if parent[adj] == -1:
                parent[adj] = node  # 부모 기록
                stack.append(adj)  # 스택에 추가


# 스택을 이용한 DFS 실행
dfs_stack(1)

for i in range(2, N + 1):
    print(parent[i])
