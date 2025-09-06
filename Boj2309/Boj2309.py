import sys

data = [sys.stdin.readline().strip() for i in range(9)]
heights = list(map(int, data))


def find(arr: list, i: int, current_arr: list) -> list:
    if len(current_arr) == 7:
        if sum(current_arr) == 100:
            return current_arr
        else:
            return []
    if i >= 9:
        return []

    # 선택한다 (리스트 복사해서 새로운 리스트로 전달)
    select_arr = find(arr, i + 1, current_arr + [arr[i]])
    if select_arr:
        return select_arr

    # 선택하지 않는다
    pass_arr = find(arr, i + 1, current_arr)
    if pass_arr:
        return pass_arr

    return []


ans = find(heights, 0, list())
ans.sort()
for height in ans:
    print(height)
