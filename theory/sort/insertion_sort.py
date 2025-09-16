from typing import MutableSequence


def insertion_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(1, n):
        j = i
        temp = a[i]
        while j > 0 and a[j - 1] > temp:
            a[j] = a[j - 1]
            j -= 1
        a[j] = temp


if __name__ == "__main__":
    arr = [6, 4, 8, 3, 1, 9, 7]
    insertion_sort(arr)
    print(arr)
