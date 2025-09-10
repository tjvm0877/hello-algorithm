import sys


input = lambda: sys.stdin.readline().rstrip()

n = int(input())

for i in range(n):
    l = input()
    continuity = 1  # 연속으로 맞춘 횟수
    total_score = 0  # 총 점수
    for isAnswer in l:
        if isAnswer == "O":
            total_score += continuity
            continuity += 1
        else:
            continuity = 1

    print(total_score)
