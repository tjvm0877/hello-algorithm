import sys


input = lambda: sys.stdin.readline().rstrip()


def binary_search(trees, target):
    left, right = 0, max(trees)
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        total = sum(tree - mid for tree in trees if tree > mid)
        if total >= target:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    return answer


# 입력 및 출력 예시
N, M = map(int, input().split())
trees = list(map(int, input().split()))
print(binary_search(trees, M))
