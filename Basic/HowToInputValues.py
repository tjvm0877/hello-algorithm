# input()
# 사용자로부터 한 줄의 문자열 입력을 받는 함수
# 입력값은 무조건 문자열(str) 타입으로 반환

a = input()  # 문자열을 입력받음
a = int(input())  # 입력받은 문자열을 정수로 변환? 변경?

# split()
# 문자열을 공백(기본값) 또는 지정한 구분자로 쪼개서 리스트로 반환
# 구분자는 인자(Argument)로 넘겨주면된다.
# 예를 들어, 입력값이 "10 20"이라면, input().split()은 ["10", "20"] 리스트를 만듭

# map(function, iterable)
# iterable의 각 요소에 function을 적용하여 결과를 뽑아내는 내장 함수
# "10 20"이 입력되면 map(int, ["10", "20"])이 되어, 리스트 안 문자열 각각을 정수로 변환
a = input().split()
a, b = input().split()
a, b = map(int, input().split())

# ----------------------------------------

# 빠른 입출력
# https://djm03178.tistory.com/21
import sys

# sys.stdin.readline()은 매 줄의 끝에 있는 개행 문자를 포함하여 반환
# input() 함수를 재정의하여 sys.stdin.readline()을 사용하되, 개행 문자를 제거(rstrip())
input = lambda: sys.stdin.readline().rstrip()

n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    print(a + b)

# 2차원 배열 입력받기
n = int(input())  # 행의 수

arr = []
for _ in range(n):
    row = list(map(int, input().split()))  # 각 행을 정수 리스트로 변환
    arr.append(row)
