import sys


input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    N, K = map(int, input().split())
    coins = []
    for _ in range(N):
        coins.append(int(input()))

    
    for coin in range(len(coins), -1, -1):

