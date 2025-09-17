import heapq
import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())

min_heap = [int(input()) for _ in range(N)]
heapq.heapify(min_heap)

result = 0

while len(min_heap) > 1:
    first = heapq.heappop(min_heap)
    second = heapq.heappop(min_heap)

    sum = first + second
    result += sum
    heapq.heappush(min_heap, sum)


print(result)
