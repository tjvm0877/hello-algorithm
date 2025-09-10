from typing import MutableSequence


def selection_sort(a: MutableSequence) -> None:
    n = len(a)

    for i in range(n - 1):
        min = i  # 정렬할 부분에서 가장 작은 인덱스
        for j in range(i + 1, n):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]
