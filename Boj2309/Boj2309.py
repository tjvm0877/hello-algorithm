import sys
from typing import Sequence


input = lambda: sys.stdin.readline().rstrip()
dwarfs: Sequence


def find_combinations(i, list):

    if len(list) == 7:
        if sum(list) == 100:
            return list
        else:
            return None

    if i >= 9:
        return None

    # 이번 난쟁이 선택
    select = find_combinations(i + 1, list + [dwarfs[i]])

    if select is not None:
        return select

    # 이번 난쟁이 선택 안함
    unselect = find_combinations(i + 1, list)
    if unselect is not None:
        return unselect

    return None


if __name__ == "__main__":
    dwarfs = [int(input()) for _ in range(9)]
    ans = find_combinations(0, list())
    ans.sort()
    for i in ans:
        print(i)
