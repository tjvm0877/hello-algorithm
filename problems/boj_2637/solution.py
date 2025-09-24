from collections import deque
import sys


input = lambda: sys.stdin.readline().rstrip()


n = int(input())
m = int(input())

# 역방향 인접리스트와 진입차수 배열
adj = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for _ in range(m):
    x, y, k = map(int, input().split())
    adj[x].append((y, k))  # x를 만들기 위해 y가 k개 필요
    indegree[y] += 1  # y의 진입차수 증가

# 각 부품의 필요 개수 저장
need = [0] * (n + 1)
need[n] = 1  # 완제품 1개 제작

queue = deque()
# 진입차수 0인 노드를 큐에 추가 (완제품부터 시작)
for i in range(1, n + 1):
    if indegree[i] == 0:
        queue.append(i)
while queue:
    current = queue.popleft()

    # 현재 부품을 사용하는 상위 부품들 처리
    for next_part, count in adj[current]:
        need[next_part] += need[current] * count
        indegree[next_part] -= 1

        if indegree[next_part] == 0:
            queue.append(next_part)

# 기본 부품 출력 (진출차수가 0인 부품들)
for i in range(1, n + 1):
    if len(adj[i]) == 0:  # 다른 부품을 만드는데 사용되지 않음
        print(i, need[i])
