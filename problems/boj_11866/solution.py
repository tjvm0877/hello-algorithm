from collections import deque
import sys


input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())

ans = []
q = deque([])
for i in range(1, N + 1):
    q.append(i)

while len(q) > 1:
    for i in range(K):
        if i == K - 1:
            ans.append(q.popleft())
            continue

        q.append(q.popleft())
ans.append(q.popleft())

print("<" + ", ".join(map(str, ans)) + ">")
