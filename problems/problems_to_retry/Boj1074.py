import sys

input = lambda: sys.stdin.readline().rstrip()

# 전역변수 선언
g_r = None
g_c = None


def z_search(n, r, c, count) -> int:
    global g_r, g_c  # 전역변수 사용 선언

    if n == 0:
        return count

    half = 2 ** (n - 1)
    size = half * half

    if g_r < r + half and g_c < c + half:
        return z_search(n - 1, r, c, count)
    elif g_r < r + half and g_c >= c + half:
        return z_search(n - 1, r, c + half, count + size)
    elif g_r >= r + half and g_c < c + half:
        return z_search(n - 1, r + half, c, count + (size * 2))
    else:  # g_r >= r + half and g_c >= c + half:
        return z_search(n - 1, r + half, c + half, count + (size * 3))


if __name__ == "__main__":
    N, r, c = map(int, input().split())
    g_r, g_c = r, c  # 전역변수에 값 할당
    print(z_search(N, 0, 0, 0))
