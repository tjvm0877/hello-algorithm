from typing import MutableSequence


def quick_sort(a: MutableSequence, left: int, right: int) -> None:
    pl = left
    pr = right
    x = a[(left + right) // 2]  # 피벗(가운데 원소 인덱스)

    while pl <= pr:
        while a[pl] < x:
            pl += 1
        while a[pr] > x:
            pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    if left < pr:
        quick_sort(a, left, pr)
    if pl < right:
        quick_sort(a, pl, right)
