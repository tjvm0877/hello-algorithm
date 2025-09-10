import sys
from typing import Sequence


input = lambda: sys.stdin.readline().rstrip()


def get_max_value(s: Sequence) -> list:
    index = 0
    max_value = s[index]

    for i in range(len(s)):
        if s[i] > max_value:
            max_value = s[i]
            index = i
    return [max_value, index + 1]


if __name__ == "__main__":
    numbers = [int(input()) for _ in range(9)]
    ans = get_max_value(numbers)
    print(f"{ans[0]}\n{ans[1]}")
