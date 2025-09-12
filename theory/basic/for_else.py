# 파이썬의 for-else 문법은 반복문(for)이 정상적으로 끝났을 때만 else 블록을 실행하는 문법
# for-else는 반복문이 break 없이 모두 실행됐을 때만 else 문을 실행하는 문법입
# 주로 "특정 조건이 없을 때만 마지막에 동작"이 필요한 로직에서 자주 쓰임

# 기본 구조와 동작
# for 루프 다음에 else를 붙여 사용할 가능
# for문이 break 없이 끝까지 실행되면 else 블록이 실행

# 반복 중 break가 발생하면 else 블록은 건너뜀

# 일반적인 for-else문 예시
for x in [1, 2, 3, 4]:
    if x % 3 == 0:
        break
    print(x)
else:
    print("모든 값을 확인했습니다.")

# 출력
# 1
# 2
