import sys


input = lambda: sys.stdin.readline().rstrip()

n = int(input())
matrix = tuple(tuple(map(int, input().split())) for _ in range(n))
print(matrix)


# input - 시작좌표, 끝 좌표
# output - 입력된 범위안에 하얀색, 파란색 정사각형 갯수
def count_papers(length, start):
    # 전체 순회 => 카운트
    white = 0
    blue = 0

    print(f"start = {start}")

    for i in range(start[0], start[0] + length):
        for j in range(start[1], start[1] + length):
            print(f"[{i}][{j}] = {matrix[i][j]}")
            if matrix[i][j] == 1:
                blue += 1
            else:
                white += 1
        print()

    total = [0, 0]  # [0] = white, [1] = blue
    if blue == 0:
        total[0] += 1
    elif white == 0:
        total[1] += 1

    # 자르고 입력된 범위안에 하얀색, 파란색 정사각형 갯수 카운트
    if blue != 0 and white != 0:
        print("분할해서 탐색")

        # (0,0)
        sequence = count_papers(length // 2, start)
        total[0] += sequence[0]
        total[1] += sequence[1]

        # (0,4)
        sequence = count_papers(length // 2, [start[0] + length // 2, start[1]])
        total[0] += sequence[0]
        total[1] += sequence[1]

        # (4,0)
        sequence = count_papers(length // 2, [start[0], start[1] + length // 2])
        total[0] += sequence[0]
        total[1] += sequence[1]

        # (4,4)
        sequence = count_papers(
            length // 2, [start[0] + length // 2, start[1] + length // 2]
        )
        total[0] += sequence[0]
        total[1] += sequence[1]

    return total


for ans in count_papers(n, [0, 0]):
    print(ans)
