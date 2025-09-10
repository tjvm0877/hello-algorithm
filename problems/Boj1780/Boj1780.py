import sys
from typing import MutableSequence

g_minus = 0
g_zero = 0
g_one = 0
matrix: MutableSequence

input = lambda: sys.stdin.readline().rstrip()


def is_all_same(s, row, col):
    global matrix, g_minus, g_zero, g_one

    for i in range(row, row + s):
        for j in range(col, col + s):
            if matrix[i][j] != matrix[row][col]:
                return False

    if matrix[row][col] == -1:
        g_minus += 1
    elif matrix[row][col] == 0:
        g_zero += 1
    else:
        g_one += 1

    return True


def slice(s, row, col):

    if is_all_same(s, row, col):
        return

    # 거짓이면 9개로 자르기
    next_s = s // 3
    for i in range(0, 3):
        for j in range(0, 3):
            slice(next_s, row + (next_s * i), col + (next_s * j))


if __name__ == "__main__":
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    slice(n, 0, 0)
    print(g_minus)
    print(g_zero)
    print(g_one)
