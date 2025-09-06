n, g_r, g_c = map(int, input().split())
founded = False


def z_search(n, r, c, count):
    if n == 0:
        return count
    half = 2 ** (n - 1)
    size = half * half
    if g_r < r + half and g_c < c + half:
        return z_search(n - 1, r, c, count)
    elif g_r < r + half and g_c >= c + half:
        return z_search(n - 1, r, c + half, count + size)
    elif g_r >= r + half and g_c < c + half:
        return z_search(n - 1, r + half, c, count + 2 * size)
    else:
        return z_search(n - 1, r + half, c + half, count + 3 * size)


print(z_search(n, 0, 0, 0))
