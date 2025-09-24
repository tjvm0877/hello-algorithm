import heapq
import sys

input = lambda: sys.stdin.readline().rstrip()
INF = int(1e9)


def dijkstra(graph, start, n):
    distance = [INF] * (n + 1)
    distance[start] = 0
    heap = [(0, start)]

    while heap:
        dist, now = heapq.heappop(heap)

        if distance[now] < dist:
            continue

        for next_node, cost in graph[now]:
            new_cost = dist + cost

            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(heap, (new_cost, next_node))

    return distance


# 입력 처리
n, m = map(int, input().split())
start = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 다익스트라 실행
result = dijkstra(graph, start, n)

# 결과 출력
for i in range(1, n + 1):
    if result[i] == INF:
        print("INFINITY")
    else:
        print(result[i])
