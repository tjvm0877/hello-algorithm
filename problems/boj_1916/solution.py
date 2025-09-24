import heapq
import sys


input = lambda: sys.stdin.readline().rstrip()
INF = float("INF")

N = int(input())  # 도시의 개수
M = int(input())  # 간선의 갯수
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))

start, end = map(int, input().split())


def dijkstra(start, graph):
    distance = [INF] * (N + 1)
    distance[start] = 0
    heap = [(start, 0)]

    while heap:
        now, dist = heapq.heappop(heap)

        if distance[now] < dist:
            continue

        for next, cost in graph[now]:
            new_cost = dist + cost

            if new_cost < distance[next]:
                distance[next] = new_cost
                heapq.heappush(heap, (next, new_cost))
    return distance


distance = dijkstra(start, graph)
print(distance[end])
