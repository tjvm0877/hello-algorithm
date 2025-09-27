from collections import deque
import sys


input = lambda: sys.stdin.readline().rstrip()


def dfs(row, col, visited, matrix):
    stack = deque()
    stack.append((row, col))

    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

    ans = 0
    while stack:

        cur_row, cur_col = stack.pop()

        if visited[cur_row][cur_col] != 0:
            continue

        visited[cur_row][cur_col] = 1
        ans += 1

        for direction in directions:
            n_row = cur_row + direction[0]
            n_col = cur_col + direction[1]

            if (n_row < 0 or n_row >= n) or (n_col < 0 or n_col >= n):
                continue

            if matrix[n_row][n_col] == "0" or visited[n_row][n_col] != 0:
                continue
            stack.append((n_row, n_col))
    return ans


if __name__ == "__main__":
    n = int(input())
    matrix = []
    for _ in range(n):
        matrix.append(list(input()))
    visited = [[0] * n for _ in range(n)]

    ans = []
    for row in range(n):
        for col in range(n):
            if visited[row][col] != 0:
                continue

            if matrix[row][col] == "0":
                continue

            dong = dfs(row, col, visited, matrix)
            if dong != 0:
                ans.append(dong)

    ans.sort()
    print(len(ans))
    for i in ans:
        print(i)
