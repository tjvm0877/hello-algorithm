from collections import deque


n = int(input())
matrix = []
for _ in range(n):
    line = list(map(int, list(input())))
    matrix.append(line)

# 거리 배열 초기화
dist = [[float("inf")] * n for _ in range(n)]
dist[0][0] = 0 if matrix[0][0] == 1 else 1

# 덱 사용 (앞쪽: 가중치 0, 뒤쪽: 가중치 1)
dq = deque([(0, 0)])

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

while dq:
    x, y = dq.popleft()

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if 0 <= nx < n and 0 <= ny < n:
            # 현재까지 비용 + 다음 방의 변경 비용
            cost = 0 if matrix[nx][ny] == 1 else 1
            new_dist = dist[x][y] + cost

            # 더 짧은 경로 발견시 갱신
            if new_dist < dist[nx][ny]:
                dist[nx][ny] = new_dist

                # 가중치에 따라 덱의 앞/뒤 삽입
                if cost == 0:
                    dq.appendleft((nx, ny))  # 가중치 0
                else:
                    dq.append((nx, ny))  # 가중치 1

print(dist[n - 1][n - 1])
