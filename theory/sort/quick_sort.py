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


if __name__ == "__main__":
    arr = [5, 8, 4, 2, 6, 1, 3, 9, 7]
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)
