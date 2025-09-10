# 파이썬에서 시작과 끝에 언더스코어(_)가 2개 붙은 함수는 특별한 의미가 있음
# 밑줄이 2개인 더블 언더 스코어(double underscore)를 줄여서 던더(dunder)라고함
# 더블 언더스코어 함수를 줄여서 던더함수라고하고, __len()__을 던더 랜 던더,, 또는 던더 렌 이라고함

from typing import Any


class MyList:

    def __init__(self, items):
        self.items = items

    # 클래스형의 인스턴스를 len()함수에 전달 가능
    # 예를 들어 클래스형의 인스턴스 obj에 대한 __len()__함수를 호출하는 obj.__len__()를 간단히 len(obj)로 작성 가능
    def __len__(self):
        return len(self.items)

    def count(self, value: Any) -> Any:
        c = 0
        for item in self.items:
            if value == item:
                c += 1
        return c

    # 클래스형의 인스턴스에 맴버십 판단 연산자인 in을 적용 가능
    # 예를들어 클래스형의 인스턴스 obj에 대한 __contains()__함수를 호출하는 obj.__contains__(x)를 간단히 x in obj로 작성 가능
    def __contains__(self, value: Any) -> Any:
        return self.count(value) > 0


my_list = MyList([1, 2, 3, 4])
print(len(my_list))  # 출력: 4
