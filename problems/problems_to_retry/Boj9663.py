def nQueen(depth):
    global N, arr, count
    if depth == N:
        count += 1
        return
    for i in range(N):
        arr[depth] = i
        if check(depth):
            nQueen(depth + 1)


def check(depth):
    global arr
    for i in range(depth):
        if arr[depth] == arr[i]:
            return False
        if abs(depth - i) == abs(arr[depth] - arr[i]):
            return False
    return True


if __name__ == "__main__":
    import sys

    input = sys.stdin.readline
    N = int(input())
    arr = [0] * N
    count = 0
    nQueen(0)
    print(count)
