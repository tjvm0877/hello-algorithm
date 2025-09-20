from collections import deque
import sys

sys.setrecursionlimit(10 * 6)
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
graph = [[] for _ in range(N + 1)]


parent = [0] * (N + 1)
bfs_parent = [-1] * (N + 1)

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(node, p):
    for adj in graph[node]:
        if adj != p:
            parent[adj] = node
            dfs(adj, node)


def bfs():
    queue = deque()
    queue.append(1)

    while queue:
        p = queue.popleft()
        for adj in graph[p]:
            if bfs_parent[adj] != -1:
                continue
            bfs_parent[adj] = p
            queue.append(adj)


dfs(1, 0)
# bfs()

for i in range(2, N + 1):
    print(parent[i])


# for i in range(2, N + 1):
#     print(bfs_parent[i])
