def get_max_size(arr: list):
    max_size = 0
    size = 0
    for i in range(len(arr)):
        if i == len(arr) - 1:
            size += 1
            max_size = max(size, max_size)
        elif arr[i] == 0:
            size += 1
        elif arr[i] == 1:
            size += 1
            max_size = max(size, max_size)
            size = 0
    return max_size


x, y = map(int, input().split())
times = int(input())
x_arr = [0 for i in range(x)]
y_arr = [0 for i in range(y)]

# 자르기
for i in range(times):
    direction, location = map(int, input().split())
    if direction == 1:
        x_arr[location - 1] = 1
    else:
        y_arr[location - 1] = 1


# 가장 넓은 종이 찾기
x_max = get_max_size(x_arr)
y_max = get_max_size(y_arr)
print(x_max * y_max)
