import sys

input = lambda: sys.stdin.readline().rstrip()

dwarfs = [int(input()) for _ in range(9)]
ans = []


def find_combination(start, c, total):
    # 선택한 7명에 도달했을 때 합 체크
    if len(c) == 7:
        if total == 100:
            ans.extend(c)
            return True
        else:
            return False

    for i in range(start, 9):
        c.append(dwarfs[i])
        if find_combination(i + 1, c, total + dwarfs[i]):
            return True
        c.pop()
    return False


find_combination(0, [], 0)

for dwarf in sorted(ans):
    print(dwarf)
