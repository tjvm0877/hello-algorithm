import sys


if __name__ == "__main__":
    input = lambda: sys.stdin.readline().rstrip()
    A, K = map(int, input().split())
    arr = list(map(int, input().split()))

    arr.sort()
    print(arr[K - 1])
