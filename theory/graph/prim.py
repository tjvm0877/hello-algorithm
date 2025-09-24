import heapq


def prim(graph, start):
    visited = set()
    q = [(0, start)]  # (가중치, 정점)
    result = 0

    while q:
        weight, v = heapq.heappop(q)
        if v not in visited:
            visited.add(v)
            result += weight

            for w, next_v in graph[v]:
                if next_v not in visited:
                    heapq.heappush(q, (w, next_v))
    return result
