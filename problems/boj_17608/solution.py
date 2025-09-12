from collections import deque
import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
stack = deque([])
for _ in range(N):
    length = int(input())
    while stack and stack[-1] <= length:
        stack.pop()
    stack.append(length)
print(len(stack))
