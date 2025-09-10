import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
numbers = list(map(int, input().split()))

count = 0

for num in numbers:
    if num == 1:
        continue
    is_prime_number = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime_number = False
            break
    if is_prime_number:
        count += 1

print(count)
