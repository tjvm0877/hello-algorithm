import bisect
import sys
from typing import List

sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip()


def get_longest_increasing_subsequence(nums: List[int]):
    li = []
    for i in nums:
        if not li or i > li[-1]:
            li.append(i)
        else:
            li[bisect.bisect_left(li, i)] = i
        print(f"i = {i}")
        print(li)
    return len(li)


def binary_search(x, left, right):
    if left >= right:
        return left
    mid = (left + right) // 2
    if arr[mid] < x:
        return binary_search(x, mid + 1, right)
    else:
        return binary_search(x, left, mid - 1)


n = int(input())
arr = list(map(int, input().split()))
print(get_longest_increasing_subsequence(arr))
