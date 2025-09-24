from collections import deque

n = int(input())
matrix = []
for _ in range(n):
    line = list(map(int, list(input())))
    matrix.append(line)

# 최단거리 배열 초기화 (모든 위치를 무한대로 설정)
dist = [[float("inf")] * n for _ in range(n)]

# 윗줄 맨 왼쪽 방은 시작방으로서 항상 흰 방이고
# 아랫줄 맨 오른쪽 방은 끝방으로서 역시 흰 방
dist[0][0] = 0

queue = deque([(0, 0)])

# 상하좌우 이동을 위한 방향 변경 값
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# BFS 실행
while queue:

    # 덱의 앞쪽에서 현재 위치 추출 (가장 작은 거리를 가진 노드부터 처리)
    row, col = queue.popleft()

    # 현재 거리 배열 출력 (디버깅용)
    print("-------------------------")
    print(f"[변경 전]현재 위치 = [{row}][{col}]")
    for a in dist:
        print(a)
    print()

    # 현재 위치에서 4방향으로 탐색
    for d_row, d_col in directions:
        n_row, n_col = row + d_row, col + d_col

        # 배열 범위 내에 있는지 확인
        if 0 <= n_row < n and 0 <= n_col < n:
            # 이동 비용 계산: 1(통로)이면 0, 0(벽)이면 1
            cost = 0 if matrix[n_row][n_col] == 1 else 1
            # 현재 위치까지의 거리 + 다음 위치로의 이동 비용
            new_dist = dist[row][col] + cost

            # 더 짧은 경로를 발견했을 때만 갱신
            if new_dist < dist[n_row][n_col]:
                dist[n_row][n_col] = new_dist
                queue.append((n_row, n_col))

    # 현재 거리 배열 출력 (디버깅용)
    print(f"[변경 후]현재 위치 = [{row}][{col}]")
    for a in dist:
        print(a)
    print("-------------------------")
    print("\n")

# 목적지 (n-1, n-1)까지의 최단 거리 출력
print(dist[n - 1][n - 1])
