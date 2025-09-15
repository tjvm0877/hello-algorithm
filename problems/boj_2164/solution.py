import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
q = deque(range(1, N + 1))

while len(q) > 1:
    q.popleft()
    q.append(q.popleft())

print(q.popleft())
