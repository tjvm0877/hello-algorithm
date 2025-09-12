from collections import deque
import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
towers = list(map(int, input().split()))
stack = deque([])
ans = [0] * N

stack.append((0, towers[0]))

for i in range(1, N):
    while stack and stack[-1][1] < towers[i]:
        stack.pop()

    if stack:
        ans[i] = stack[-1][0] + 1
    else:
        ans[i] = 0

    stack.append((i, towers[i]))

print(*ans)
