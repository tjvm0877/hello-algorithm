from collections import deque


adjacency_matrix = [
    [0, 1, 1, 0, 0, 0],  # A
    [0, 0, 0, 1, 1, 0],  # B
    [0, 0, 0, 0, 0, 1],  # C
    [0, 0, 0, 0, 0, 0],  # D
    [0, 0, 0, 0, 0, 1],  # E
    [0, 0, 0, 0, 0, 0],  # F
]


visited = [False] * len(adjacency_matrix)


def dfs(start):
    stack = [start]

    while stack:
        node = stack.pop()
        if not visited[node]:
            print(chr(node + 65), end=" ")
            visited[node] = True

            for i in range(len(adjacency_matrix[node]) - 1, -1, -1):
                if adjacency_matrix[node][i] == 1 and not visited[i]:
                    stack.append(i)


print("DFS 방문 순서 (스택, 인접 행렬):")
dfs(0)  # A부터 시작
print()
