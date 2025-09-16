from typing import MutableSequence, Sequence


def bubble_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n - 1):
        for j in range(n - 1, i, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]


if __name__ == "__main__":
    arr = [1, 8, 4, 3, 13, 2, 7, 9, 10]
    bubble_sort(arr)
    print(arr)
