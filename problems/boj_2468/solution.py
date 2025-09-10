import sys

sys.setrecursionlimit(10**6)  # 재귀 제한을 늘림
input = lambda: sys.stdin.readline().rstrip()


def dfs(row, col, height):
    if visited[row][col] or matrix[row][col] <= height:
        return False

    visited[row][col] = True

    stack = [(row, col)]

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while stack:
        s_row, s_col = stack.pop()
        for dr, dc in directions:
            nr, nc = s_row + dr, s_col + dc
            if 0 <= nr < N and 0 <= nc < N:
                if matrix[nr][nc] > height and visited[nr][nc] == False:
                    visited[nr][nc] = True
                    stack.append((nr, nc))
    return True


N = int(input())
matrix = tuple(tuple(map(int, input().split())) for _ in range(N))
visited = []  # 방문 여부를 표시하는 2차원 리스트
max_area = 0  # 최대 영역 갯수

for height in range(0, 100):
    visited = [[False] * N for _ in range(N)]

    count = 0
    for row in range(N):
        for col in range(N):
            if dfs(row, col, height):
                count += 1
    max_area = max(max_area, count)
    if count == 0:
        break

print(max_area)
