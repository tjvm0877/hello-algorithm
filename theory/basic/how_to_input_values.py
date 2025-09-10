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

# 입력 처리 방식의 차이
# - sys.stdin.readline은 한 번에 버퍼에 데이터를 읽어와 저장. 즉, 입력을 받을 때 여러 줄 데이터를 버퍼에 미리 받고, 이후 한 줄씩 빠르게 읽어옴
# - input은 입력을 받을 때마다 사용자의 입력을 한 글자씩 버퍼에 담아 처리. 반복적인 입력 상황에서는 이 과정이 누적되어 상대적으로 느려짐

# 추가 처리 작업
# - input 함수는 내부적으로 사용자 입력을 받기 전, 출력 버퍼를 flush하여 출력 지연 현상을 방지. 또한 입력받은 문자열의 개행 문자(\n)를 자동으로 제거하는 처리도 수행
# - sys.stdin.readline은 이런 부가 작업 없이 입력받은 데이터를 그대로 반환하므로, 부가적인 시간이 소요되지 않음. 단, 개행 문자가 포함되어 있으므로 직접 .strip()이나 .rstrip() 처리가 필요할 수 있음

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
