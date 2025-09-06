n = int(input())

for i in range(n):
    str = input()
    str_arr = list(str)

    continuity = 1  # 연속으로 맞춘 횟스
    total_score = 0  # 총 점수
    for isAnswer in str_arr:
        if isAnswer == 'O':
            total_score += continuity
            continuity += 1
        else:
            continuity = 1

    print(total_score)
