from collections import deque
import sys


input = lambda: sys.stdin.readline().rstrip()

# ----- 입력 받기 -----
N = int(input())  # 보드의 크기
K = int(input())  # 사과의 갯수
k_arr = []  # 사과의 좌표
for _ in range(K):
    data = list(map(int, input().split()))
    k_arr.append(data)

L = int(input())  # 방향 횟수
l_arr = []  # 방향 변화 정보
for _ in range(L):
    seconds, direction = input().split()
    seconds = int(seconds)
    l_arr.append([seconds, direction])


# ----- 알고리즘 -----
# 방향 (오른쪽, 아래, 왼쪽, 위)
d_arr = [[0, 1], [1, 0], [0, -1], [-1, 0]]
second = 0
direction = 0
snake = deque([[0, 0]])
apples = set((x - 1, y - 1) for x, y in k_arr)  # 0-index 변환, 빠른 탐색용 집합

is_game_over = False
while not is_game_over:
    second += 1
    head = snake[-1]
    next_head = [head[0] + d_arr[direction][0], head[1] + d_arr[direction][1]]

    # 벽 충돌 검사
    if next_head[0] < 0 or next_head[0] >= N or next_head[1] < 0 or next_head[1] >= N:
        break

    # 자기 몸 충돌 검사
    if next_head in snake:
        break

    snake.append(next_head)

    # 사과 먹기
    if (next_head[0], next_head[1]) in apples:
        apples.remove((next_head[0], next_head[1]))
        # 꼬리 유지(길이 증가)
    else:
        snake.popleft()  # 꼬리 이동(길이 유지)

    # 방향 변경 처리
    if l_arr and l_arr[0][0] == second:
        _, c = l_arr.pop(0)
        if c == "L":
            direction = (direction - 1) % 4
        else:
            direction = (direction + 1) % 4

print(second)
