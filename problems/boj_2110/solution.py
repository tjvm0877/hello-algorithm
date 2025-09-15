import sys


input = lambda: sys.stdin.readline().rstrip()


def can_install(houses, C, min_dist):
    count = 1
    current = houses[0]

    for i in range(1, len(houses)):
        if houses[i] >= current + min_dist:
            count += 1
            current = houses[i]

    return count >= C


def binary_search_recursive(houses, C, start, end, result=0):
    if start > end:
        return result

    mid = (start + end) // 2

    if can_install(houses, C, mid):
        # mid 거리에서 설치 가능하면 더 큰 거리 탐색
        return binary_search_recursive(houses, C, mid + 1, end, mid)
    else:
        # 불가능하면 더 작은 거리 탐색
        return binary_search_recursive(houses, C, start, mid - 1, result)


N, C = map(int, input().split())
houses = [int(input()) for _ in range(N)]
houses.sort()

start = 1
end = houses[-1] - houses[0]

max_dist = binary_search_recursive(houses, C, start, end)
print(max_dist)
