from collections import deque

n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
virus = []

for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            # 바이러스 종류, depth, row, col
            virus.append((graph[i][j], 0, i, j))

virus.sort()
q = deque(virus)

while q:
    # 바이러스 종류, depth, row, col
    v, t, a, b = q.popleft()
    if t == s:
        break
    for dx, dy in direction:
        na = a + dx
        nb = b + dy
        if 0 <= na < n and 0 <= nb < n and graph[na][nb] == 0:
            graph[na][nb] = v
            q.append((v, t + 1, na, nb))

print(graph[x - 1][y - 1])
