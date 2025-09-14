import sys


input = lambda: sys.stdin.readline().rstrip()


def largest_rectangle_area(heights):
    stack = [-1]  # 스택에 -1을 넣어 넓이 계산이 용이하도록 함
    max_area = 0
    for i, h in enumerate(heights):
        # 현재 막대가 스택 꼭대기의 막대보다 낮거나 같으면 스택을 팝하며 넓이 계산
        while stack[-1] != -1 and heights[stack[-1]] >= h:
            height = heights[stack.pop()]
            width = i - stack[-1] - 1  # 폭 계산
            max_area = max(max_area, height * width)
        stack.append(i)
    # 스택에 남아 있는 막대들 처리
    while stack[-1] != -1:
        height = heights[stack.pop()]
        width = len(heights) - stack[-1] - 1
        max_area = max(max_area, height * width)
        if max_area == 9:
            print("hi")
    return max_area


flag = True
while flag:
    n, *arr = map(int, input().split())
    if n == 0:
        break

    n = len(arr)
    print(largest_rectangle_area(arr))
