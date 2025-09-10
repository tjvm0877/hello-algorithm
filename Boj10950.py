import sys


input = lambda: sys.stdin.readline().rstrip()
t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    print(a + b)
