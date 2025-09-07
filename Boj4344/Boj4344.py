import sys


input = lambda: sys.stdin.readline().rstrip()

n = int(input())

for t in range(n):
    input_list = list(map(int, input().split()))
    students = input_list[0]
    scores = input_list[1 : len(input_list)]
    total = 0
    for score in scores:
        total += score

    average = total / students

    ans = 0
    for score in scores:
        if score > average:
            ans += 1

    print(f"{round(ans / students * 100, 3)}%")
