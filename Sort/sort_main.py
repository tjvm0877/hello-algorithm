import random

from quick_sort import quick_sort
from insertion_sort import insertion_sort
from bubble_sort import bubble_sort


n = 10
numbers = [random.randint(1, 100) for _ in range(n)]
print(numbers)


print("\n=== Bubble Sort ===")
bubble_sort(numbers)
print(numbers)


print("\n=== Insertion Sort ===")
insertion_sort(numbers)
print(numbers)

print("\n=== Quick Sort ===")
quick_sort(numbers, 0, n - 1)
print(numbers)
