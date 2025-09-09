from enum import Enum
from typing import Any

from networkx import is_empty


class FixedQueue:

    class Empty(Exception):
        pass

    class Full(Exception):
        pass

    def __init__(self, capacity: int) -> None:
        """큐 초기화"""
        self.no = 0  # 현재 데이터 개수
        self.front = 0  # 맨 앞 원소 커서
        self.rear = 0  # 맨 끝 원소 커서
        self.capacity = capacity  # 큐의 크기
        self.queue = [None] * capacity  # 큐의 본체

    def __len__(self) -> int:
        """큐에 있는 모든 데이터 개수를 반환"""
        return self.no

    def is_empty(self) -> bool:
        """큐가 비어있는지 판단"""
        return self.no <= 0

    def is_full(self) -> bool:
        """큐가 가득 차있는지 판단"""
        return self.no >= self.capacity

    def enque(self, x: Any) -> None:
        """데이터 x를 인큐"""
        if self.is_full():
            raise FixedQueue.Full

        self.queue[self.rear] = x
        self.rear += 1
        self.no += 1
        if self.rear == self.capacity:
            self.rear = 0

    def deque(self) -> Any:
        """데이터를 디큐"""
        if self.is_empty:
            raise FixedQueue.Empty

        x = self.queue[self.front]
        self.front += 1
        self.no -= 1
        if self.front == self.capacity:
            self.front = 0
        return x

    def peek(self) -> Any:
        """큐에서 데이터를 피크"""
        if self.is_empty:
            raise FixedQueue.Empty

        return self.queue[self.front]

    def find(self, value: Any) -> Any:
        """큐에서 value를 찾아 인덱스를 반환(없으면 -1반환)"""
        for i in range(self.no):
            idx = (i + self.front) % self.capacity
            if self.queue[idx] == value:
                return idx
        return -1

    def count(self, value: Any) -> int:
        """큐에 있는 value의 갯수를 판단"""
        c = 0
        for i in range(self.no):
            idx = (i + self.front) % self.capacity
            if self.queue[idx] == value:
                c += 1
        return c

    def __contains__(self, value: Any) -> bool:
        """큐에 value가 있는지 판단"""
        return self.count(value) > 0

    def clear(self) -> None:
        """큐의 모든 데이터를 지움"""
        self.no = self.front = self.rear = 0

    def dump(self) -> None:
        """모든 데이터를 front부터 rear까지 출력"""
        if self.is_empty:
            print("큐가 비었습니다.")
        else:
            for i in range(self.no):
                print(self.queue[(i + self.front) % self.capacity], end="")
            print()
