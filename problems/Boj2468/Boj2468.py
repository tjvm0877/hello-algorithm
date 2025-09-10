import sys

n = int(sys.stdin.readline().strip())
sys.setrecursionlimit(10**6)  # 재귀 제한을 늘림
matrix = []
for _ in range(n):
    row = list(map(int, sys.stdin.readline().split()))  # 한 줄씩 정수를 리스트로 변환
    matrix.append(row)


def dfs(visited, row, col, level):

    if matrix[row][col] <= level or visited[row][col] == 1:
        return False

    visited[row][col] = 1

    # 아래
    if row + 1 < n:
        dfs(visited, row + 1, col, level)

    # 위
    if row - 1 >= 0:
        dfs(visited, row - 1, col, level)

    # 좌
    if col - 1 >= 0:
        dfs(visited, row, col - 1, level)

    # 우
    if col + 1 < n:
        dfs(visited, row, col + 1, level)

    return True


max_land = 0
max_height = max(max(row) for row in matrix)
for i in range(max_height + 1):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    count = 0
    for j in range(n):
        for k in range(n):
            if dfs(visited, j, k, i) is True:
                count += 1

    max_land = max(count, max_land)

    if count == 0:
        break
print(max_land)
