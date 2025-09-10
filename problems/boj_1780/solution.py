import sys


input = lambda: sys.stdin.readline().rstrip()


g_m = 0
g_z = 0
g_o = 0


def count_paper(length, r, c):
    # 배열의 모든 값이 같은지 확인
    if is_useable(length, r, c):
        return

    next_length = length // 3
    for row in range(3):
        for col in range(3):
            count_paper(next_length, r + (next_length * row), c + (next_length * col))
    return


def is_useable(length, r, c):
    global matrix, g_m, g_z, g_o

    if length != 1:
        for row in range(r, r + length):
            for col in range(c, c + length):
                if matrix[row][col] != matrix[r][c]:
                    return False

    if matrix[r][c] == -1:
        g_m += 1
    elif matrix[r][c] == 0:
        g_z += 1
    else:
        g_o += 1

    return True


N = int(input())
matrix = tuple(tuple(map(int, input().split())) for _ in range(N))
count_paper(N, 0, 0)

print(g_m)
print(g_z)
print(g_o)
