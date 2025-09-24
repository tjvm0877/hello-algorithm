import heapq
import sys

input = lambda: sys.stdin.readline().rstrip()

v, e = map(int, input().split())
graph = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

visited = set()
result = 0
q = [(0, 1)]

while q:
    weight, node = heapq.heappop(q)

    if node in visited:
        continue

    visited.add(node)
    result += weight

    for next_node, cost in graph[node]:
        if next_node not in visited:
            heapq.heappush(q, (cost, next_node))

print(result)
