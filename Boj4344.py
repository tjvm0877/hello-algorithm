n = int(input())

for t in range(n):
    scores = list(map(int, input().split()))
    total = 0
    num = scores[0]
    for i in range(1, len(scores)):
        score = scores[i]
        total += score
    average = total / num

    student = 0
    for i in range(1, len(scores)):
        score = scores[i]
        if score > average:
            student += 1

    print(f"{round(student / num * 100, 3)}%")
    # print(f"{(student / num * 100):.3f}%")
1
