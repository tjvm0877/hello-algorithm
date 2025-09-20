from collections import deque
import sys

input = lambda: sys.stdin.readline().rstrip()
N, K = map(int, input().split())
str_num = input()

stack = deque([])

for i in range(N):
    num = int(str_num[i])
    while K > 0 and stack and stack[-1] < num:
        stack.pop()
        K -= 1
    stack.append(num)

# 남아있는 K를 끝에서부터 제거
while K > 0:
    stack.pop()
    K -= 1

print("".join(str(x) for x in stack))
