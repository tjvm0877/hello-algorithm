from collections import deque
import sys

input = lambda: sys.stdin.readline().rstrip()


def dfs(start, adj_list, color):
    stack = deque([start])
    color[start] = 1

    while stack:
        node = stack.pop()
        current_color = color[node]
        next_color = 2 if current_color == 1 else 1

        for neighbor in adj_list[node]:
            if color[neighbor] == 0:  # 아직 방문하지 않은 노드
                color[neighbor] = next_color
                stack.append(neighbor)
            elif color[neighbor] == current_color:  # 인접한 노드가 같은 색
                return False
    return True


t = int(input())

for _ in range(t):
    v, e = map(int, input().split())
    adj_list = [[] for _ in range(v + 1)]
    color = [0] * (v + 1)

    for _ in range(e):
        s, d = map(int, input().split())
        adj_list[s].append(d)
        adj_list[d].append(s)

    is_bipartite = True

    # 모든 노드를 확인하여 연결되지 않은 컴포넌트도 처리
    for i in range(1, v + 1):
        if color[i] == 0:  # 아직 방문하지 않은 노드
            if not dfs(i, adj_list, color):
                is_bipartite = False
                break

    print("YES" if is_bipartite else "NO")
