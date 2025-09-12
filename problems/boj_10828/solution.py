from collections import deque
import sys

input = lambda: sys.stdin.readline().rstrip()
stack = deque([])


def push(x: int):
    stack.append(x)


def pop():
    if len(stack) == 0:
        return -1
    return stack.pop()


def size():
    return len(stack)


def empty():
    return int(len(stack) == 0)


def top():
    if len(stack) == 0:
        return -1
    return stack[-1]


N = int(input())

for _ in range(N):
    command = tuple(input().split())
    if command[0] == "push":
        push(int(command[1]))
    elif command[0] == "pop":
        print(pop())
    elif command[0] == "size":
        print(size())
    elif command[0] == "empty":
        print(empty())
    elif command[0] == "top":
        print(top())
