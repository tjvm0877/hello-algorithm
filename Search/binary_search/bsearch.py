from typing import Any, Sequence


def binary_search(a: Sequence, key: Any) -> int:
    """시퀀스 a에서 key와 일치하는 원소를 이진 검색"""
    pl = 0
    pr = len(a) - 1

    while True:
        pc = (pl + pr) // 2

        if a[pc] == key:
            return pc  # 검색 성공
        elif a[pc] < key:
            pr = pc - 1
        # elif a[pc] > key:
        else:
            pl = pc + 1

        if pl > pr:
            break

    return -1  # 검색 실패
