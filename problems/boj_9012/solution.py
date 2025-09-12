from collections import deque
import sys


input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    stack = deque([])
    ps = input()
    for s in ps:
        if s == "(":
            stack.append(0)
        else:
            if (len(stack)) == 0:
                print("No")
                break
            stack.pop()
    else:
        if stack:
            print("NO")
        else:
            print("YES")
