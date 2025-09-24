from collections import deque
import sys

input = lambda: sys.stdin.readline().rstrip()

n, m, k, x = map(int, input().split())
adj_list = [[] for _ in range(n + 1)]

for _ in range(m):
    s, d = map(int, input().split())
    adj_list[s].append(d)

ans = []
q = deque([(x, 0)])
visited = [False] * (n + 1)
visited[x] = True

while q:
    now, dist = q.popleft()

    # 목표 거리에 도달한 경우
    if dist == k:
        ans.append(now)
        continue  # 더 이상 진행하지 않음

    # 거리 제한 체크 (조기 종료)
    if dist >= k:
        continue

    # 인접 노드 탐색
    for next_node in adj_list[now]:
        if not visited[next_node]:
            visited[next_node] = True
            q.append((next_node, dist + 1))

# 결과 출력
if not ans:
    print(-1)
else:
    ans.sort()
    for node in ans:
        print(node)
