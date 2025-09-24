from collections import deque
import sys


input = lambda: sys.stdin.readline().split()

n, m, v = map(int, input())


adj_list = [[] for _ in range(n)]
dfs_list = []
bfs_list = []

for _ in range(m):
    s, d = map(int, input())
    adj_list[s - 1].append(d)
    adj_list[d - 1].append(s)


def dfs(source):
    stack = deque()
    stack.append(source)
    visited = [-1] * n

    while stack:
        node = stack.pop()
        if visited[node - 1] != -1:
            continue

        dfs_list.append(node)
        visited[node - 1] = 1

        adj_list[node - 1].sort(reverse=True)
        for next in adj_list[node - 1]:
            stack.append(next)


def bfs(source):
    queue = deque()
    queue.append(source)
    visited = [-1] * n

    while queue:
        node = queue.popleft()
        if visited[node - 1] != -1:
            continue

        bfs_list.append(node)
        visited[node - 1] = 1

        adj_list[node - 1].sort()
        for next in adj_list[node - 1]:
            queue.append(next)


dfs(v)
bfs(v)

print(*dfs_list)
print(*bfs_list)
