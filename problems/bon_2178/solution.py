from collections import deque
import sys

input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
matrix = []

for _ in range(n):
    line = list(map(int, list(input())))
    matrix.append(line)

col = (0, 0, -1, 1)
row = (-1, 1, 0, 0)

queue = deque()
queue.append((0, 0))
matrix[0][0] = 1  # 출발점 거리 1로 초기화

while queue:
    cur_row, cur_col = queue.popleft()
    for i in range(4):
        next_row = cur_row + row[i]
        next_col = cur_col + col[i]

        if next_row < 0 or next_row >= n:
            continue
        if next_col < 0 or next_col >= m:
            continue

        # 이동 가능한 길이고 방문하지 않은 경우 (값이 1인 경우)
        if matrix[next_row][next_col] == 1:
            matrix[next_row][next_col] = matrix[cur_row][cur_col] + 1
            queue.append((next_row, next_col))

print(matrix[n - 1][m - 1])
