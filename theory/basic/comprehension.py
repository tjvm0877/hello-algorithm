# Comprehension: 파이썬에서 내포 표기 생성은 반복문과 조건문을 간결하게 사용해서 리스트, 세트, 딕셔너리와 같은 컬렉션 객체를 효율적으로 생성하는 문법

# ---------- List ----------
numbers = [1, 2, 3, 4, 5]

# numbers의 홀수 원자값을 *2한 리스트 생성
twice_list = [num * 2 for num in numbers if num % 2 == 1]

# 파이썬 튜플 자체에는 리스트 내포(list comprehension)처럼 직접적으로 내포표기 생성 문법은 없음
# 하지만 튜플 내포를 흉내 낼 때는 **제너레이터 표현식(generator expression)**을 사용하고, 그 결과를 다시 tuple() 함수로 감싸서 튜플을 만듬
twice_tuple = tuple(num * 2 for num in numbers if num % 2 == 1)

print(twice_list)
print(twice_tuple)
