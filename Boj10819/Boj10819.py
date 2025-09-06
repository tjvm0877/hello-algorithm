# |A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|
import sys

n = int(sys.stdin.readline().strip())  # 첫 줄: 숫자 개수
data = list(map(int, sys.stdin.readline().split()))

is_used = [1 for _ in range(n)]
arr = [0 for _ in range(n)]


# arr = 1~6을 조합해서 만든조합해서 만든 배열
def recursion(pos, arr, is_used):
    global n
    if pos >= n:
        result = 0
        for j in range(1, n):
            result += abs(data[arr[j - 1]] - data[arr[j]])
        return result

    local_max = -sys.maxsize - 1

    for i in range(n):
        # 넣고
        if is_used[i] == 0:
            continue

        arr[pos] = i
        is_used[i] = 0

        # 값 얻기
        value = recursion(pos + 1, arr, is_used)
        local_max = max(value, local_max)

        # 빼고
        is_used[i] = 1

    return local_max


print(recursion(0, arr, is_used))
