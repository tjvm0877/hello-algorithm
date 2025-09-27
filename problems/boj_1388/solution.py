from collections import deque
import sys


def dfs(row, col, graph, visited):
    if visited[row][col] != 0:
        return 0

    stack = deque()
    stack.append((row, col))

    while stack:
        cur_row, cur_col = stack.pop()

        visited[cur_row][cur_col] = 1

        if graph[cur_row][cur_col] == "-":
            next_col = cur_col + 1
            if next_col >= 0 and next_col < m and graph[row][next_col] == "-":
                stack.append((row, next_col))

        elif graph[cur_row][cur_col] == "|":
            next_row = cur_row + 1
            if next_row >= 0 and next_row < n and graph[next_row][col] == "|":
                stack.append((next_row, col))

    return 1


if __name__ == "__main__":
    input = lambda: sys.stdin.readline().rstrip()
    n, m = map(int, input().split())
    graph = []
    visited = [[0] * m for _ in range(n)]
    for _ in range(n):
        graph.append(list(input()))

    ans = 0
    for row in range(n):
        for col in range(m):
            ans += dfs(row, col, graph, visited)

    print(ans)
