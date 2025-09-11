import sys

n = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(n)]

n = int(data[0])  # 첫 번째 값이 n개수
nums = list(map(int, data))

nums.sort()

# for num in nums:
#     print(num)
print('\n'.join(map(str, nums)))
