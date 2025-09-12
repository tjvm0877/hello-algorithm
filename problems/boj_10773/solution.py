from collections import deque
import sys


input = lambda: sys.stdin.readline().rstrip()

K = int(input())
stack = deque([])

for _ in range(K):
    n = int(input())
    if n == 0:
        stack.pop()
        continue
    stack.append(n)

ans = 0
print(sum(stack))
