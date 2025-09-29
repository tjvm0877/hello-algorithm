import sys

input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    N, K = map(int, input().split())
    coins = []
    for _ in range(N):
        coins.append(int(input()))

    ans = 0
    index = N - 1
    while K > 0:
        if K >= coins[index]:
            ans += K // coins[index]
            K = K % coins[index]
        index -= 1

    print(ans)
