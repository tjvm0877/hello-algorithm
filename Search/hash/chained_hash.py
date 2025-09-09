from __future__ import annotations
import hashlib
from typing import Any, List, Optional


class Node:
    """해시를 구성하는 노드"""

    def __init__(self, key: Any, value: Any, next: Optional[Node]) -> None:
        """초기화"""
        self.key = key
        self.value = value
        self.next = next


class ChainedHash:
    """체인법으로 해시 클래스 구현"""

    # capaticy: 해시 테이블의 크기(배열 table의 원소 수)
    # table: 해시 테이블을 저장하는 list형 배열

    def __init__(self, capacity: int) -> None:
        """초기화, 빈 해시 테이블을 생성"""

        self.capacity = capacity  # 해시 테이블의 크기를 지정

        # 해시 테이블(리스트) 선언
        self.table: List[Optional[Node]] = [None] * self.capacity

    def hash_value(self, key: Any) -> int:
        """해시값을 구함"""
        if isinstance(key, int):
            return key % self.capacity
        # haxdigest() : sha256알고리즘에서 해시값을 16진수 문자열로 꺼냄
        return (int(hashlib.sha256(str(key).encode()).hexdigest(), 16)) % self.capacity

    def search(self, key: Any) -> Any:
        """키가 key인 원소를 검색하여 값을 반환"""
        hash = self.hash_value(key)
        p = self.table[hash]

        while p is not None:
            if p.key == key:
                return p.value
            p = p.next

        return None

    def add(self, key: Any, value: Any) -> bool:
        """키가 key이고 값이 value인 원소를 추가"""
        hash = self.hash_value(key)
        p = self.table[hash]

        # 기존 키가 있는지 확인하고 값 업데이트
        while p is not None:
            if p.key == key:
                p.value = value  # 기존 값 업데이트
                return False  # 새로 추가하지 않았으므로 False
            p = p.next

        # 새 노드를 체인의 맨 앞에 추가
        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp
        return True  # 새로 추가했으므로 True

    def remove(self, key: Any) -> bool:
        """키가 key인 원소를 삭제"""
        hash = self.hash_value(key)  # 삭제할 key의 해시값
        p = self.table[hash]
        pp = None  # 바로 앞의 노드

        while p is not None:
            if p.key == key:  # 키를 발견하면
                if pp is None:
                    self.table[hash] = p.next
                else:
                    pp.next = p.next
                return True  # key 삭제 성공

            pp = p
            p = p.next

        return False

    def dump(self) -> None:
        """모든 해시 테이블을 덤프(해시테이블의 내용을 한꺼번에 통체로 출력)"""
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end="")
            while p is not None:
                print(f"    -> {p.key} ({p.value})", end="")
                p = p.next
            print()
