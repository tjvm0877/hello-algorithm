import sys

n = int(sys.stdin.readline().strip())
sys.setrecursionlimit(10000)  # 재귀 제한을 늘림
matrix = []
for _ in range(n):
    row = list(map(int, sys.stdin.readline().split()))  # 한 줄씩 정수를 리스트로 변환
    matrix.append(row)

# 잠기지 않은 구역을 카운트해주는 함수가 있어야겠는데...


def dfs(visited, start_row, start_col, level):
    if matrix[start_row][start_col] <= level or visited[start_row][start_col] == 1:
        return False

    stack = [(start_row, start_col)]
    visited[start_row][start_col] = 1

    while stack:
        row, col = stack.pop()

        # 상하좌우 방향
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if 0 <= nr < n and 0 <= nc < n:
                if matrix[nr][nc] > level and visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    stack.append((nr, nc))

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
