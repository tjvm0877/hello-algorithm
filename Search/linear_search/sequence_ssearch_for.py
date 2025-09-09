from typing import Any, Sequence


def seq_search(a: Sequence, key: Any) -> int:
    """시퀀스 a에서 key와 같은 원소를 for문을 이용하여 선형 검색"""

    for i in range(len(a)):
        if a[i] == key:
            return i  # 검색 성공 (인덱스 반환)

    return -1  # 검색 실패(-1 반환)
