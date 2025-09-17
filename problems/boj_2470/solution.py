import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

left, right = 0, N - 1
min_diff = float("inf")
ans = (arr[left], arr[right])

while left < right:
    current_sum = arr[left] + arr[right]
    if abs(current_sum) < min_diff:
        min_diff = abs(current_sum)
        ans = (arr[left], arr[right])

    if current_sum == 0:
        break
    elif current_sum < 0:
        left += 1
    else:
        right -= 1

print(ans[0], ans[1])
