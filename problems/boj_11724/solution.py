from collections import deque
import sys


input = lambda: sys.stdin.readline().split()

# n = 정점의 개수, m = 간선의 갯수
n, m = map(int, input())

adj_list = [[] for _ in range(n)]
for _ in range(m):
    s, d = map(int, input())
    adj_list[s - 1].append(d)
    adj_list[d - 1].append(s)


visited = [0] * n


def dfs(source):
    stack = deque()
    stack.append(source)
    count = 0

    while stack:
        node = stack.pop()

        if visited[node - 1] == 1:
            continue

        count += 1
        visited[node - 1] = 1

        for d in adj_list[node - 1]:
            stack.append(d)

    return count


cc = 0
for i in range(n):
    if dfs(i) > 0:
        cc += 1
print(cc)
