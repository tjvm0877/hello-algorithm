from collections import deque
import sys


input = lambda: sys.stdin.readline().rstrip()

n = int(input())
m = int(input())
adj_list = [[] for _ in range(n)]
for _ in range(m):
    s, d = map(int, input().split())
    adj_list[s - 1].append(d)
    adj_list[d - 1].append(s)

visited = [0] * n


def dfs():
    stack = deque()
    stack.append(1)

    while stack:
        node = stack.pop()
        if visited[node - 1] == 1:
            continue

        visited[node - 1] = 1

        for d in adj_list[node - 1]:
            stack.append(d)


dfs()
print(sum(visited) - 1)
