import sys

# 표준 입력에서 한 줄 읽고 끝의 개행문자 제거하는 람다 함수 정의
input = lambda: sys.stdin.readline().strip()

N = int(input())  # 원의 개수 입력 받기

pointers = []
for _ in range(N):
    # 각 원의 중심 좌표와 반지름 입력 받기
    center, radius = map(int, input().split())
    # 원의 왼쪽 경계점 좌표와 오른쪽 경계점 좌표를 구해서 리스트에 추가
    pointers.append(("l", (center - radius)))  # 왼쪽 점
    pointers.append(("r", (center + radius)))  # 오른쪽 점

# l이 앞, r이 뒤로오도록 정렬
pointers.sort(key=lambda x: x[0], reverse=True)
# 좌표값 기준으로 오름차순 정렬
pointers.sort(key=lambda x: x[1])

# 공간의 최소 개수 (초기값 1)
count = 1

stack = []
for pointer in pointers:
    # 왼쪽 경계 'l'이면 스택에 넣음 (원의 시작점)
    if pointer[0] == "l":
        stack.append(pointer)
        continue

    # 오른쪽 경계 'r'이면 스택에서 원의 시작점을 꺼내며 처리
    total_width = 0
    while stack:
        prev = stack.pop()

        # 스택에서 꺼낸 것이 왼쪽 경계이면 원의 지름 계산
        if prev[0] == "l":
            width = pointer[1] - prev[1]  # 원의 지름

            # 이전에 이어진 원 크기와 같으면 count 2 증가, 아니면 1 증가
            if total_width == width:
                count += 2
            else:
                count += 1

            # 계산된 너비를 'c'로 표시하여 스택에 다시 넣음 (연결된 원 크기 합산용)
            stack.append(("c", width))
            break

        # 이전에 계산된 연결된 원 크기가 있다면 누적해서 더함
        elif prev[0] == "c":
            total_width += prev[1]

# 최종 공간 개수 출력
print(count)
