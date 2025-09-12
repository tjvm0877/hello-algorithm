from typing import Any


class FixedStack:
    """고정 길이 스택 클래스"""

    class Empty(Exception):
        """비어있는 FixedStack에 팝 또는 피크할 때 내보내는 예외 처리"""

        pass

    class Full(Exception):
        """가득 찬 FixedStack에 푸시할 때 내보내는 예외 처리"""

        pass

    def __init__(self, capacity: int = 256) -> None:
        """스택 초기화"""
        self.stack = [None] * capacity
        self.capacity = capacity
        self.ptr = 0

    def __len__(self) -> int:
        """스택에 쌓여있는 데이터 개수를 반환"""
        return self.ptr

    def is_empty(self) -> bool:
        """스택이 비어있는지 판단"""
        return self.ptr <= 0

    def is_full(self) -> bool:
        """스택이 가득 쌓였는지 판단"""
        return self.ptr >= self.capacity

    def push(self, value: Any) -> None:
        """스택에 value를 푸시(데이터를 넣음)"""
        if self.is_full():  # 스택이 가득 차있는 경우
            raise FixedStack.Full  # 에외를 발생

    def pop(self) -> Any:
        """스택에서 데이터를 피크(Top에 있는 데이터를 들여다봄)"""
        if self.is_empty:
            raise FixedStack.Empty
        return self.stack[self.ptr - 1]

    def clear(self) -> None:
        """스택을 비움(모든 데이터를 삭제)"""
        self.ptr = 0

    def find(self, value: Any) -> Any:
        """스택에서 value를 찾아 인덱스를 반환(없으면 -1을 반환)"""
        for i in range(self.ptr - 1, -1, -1):  # Top에서부터 Bottom까지 선형탐색
            if self.stack[i] == value:
                return i
        return -1

    def count(self, value: Any) -> Any:
        """스택에 있는 value의 개수를 반환"""
        c = 0
        for i in range(self.ptr):
            if self.stack[i] == value:
                c += 1
        return c

    def __contains__(self, value: Any) -> bool:
        """스택에 value가 있는지 판단"""
        return self.count(value) > 0

    def dump(self) -> None:
        """덤프(스택 안의 모든 데이터를 바닥부터 꼭대기 순으로 출력)"""
        if self.is_empty():
            print("스택이 비어있습니다.")
        else:
            print(self.stack[: self.ptr])
