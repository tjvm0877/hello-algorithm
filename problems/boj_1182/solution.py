import sys


input = lambda: sys.stdin.readline().rstrip()


def get_partition(i, sum, l):

    if i >= N:
        if sum == S and len(l) > 0:
            print(l)
            return 1
        else:
            return 0

    count = 0

    # 이번 인덱스 포함
    count += get_partition(i + 1, sum + arr[i], l + [arr[i]])

    # 이번 인덱스 미포함
    count += get_partition(i + 1, sum, l)

    return count


N, S = map(int, input().split())
arr = tuple(map(int, input().split()))
print(get_partition(0, 0, []))
