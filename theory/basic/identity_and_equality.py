# 동일성(Identity): 두 객체가 메모리에서 완전히 같은 객체인지, 즉 같은 주소를 가리키는지를 비교
# 동등성(Equality): 두 객체가 값이나 내용상 같은지를 비교
# 파이썬은 Call By Object Value
list1 = [1, 2, 3, 4, 5]
list2 = list1
list3 = [1, 2, 3, 4, 5]

# ---------- 동일성 비교 ----------
print(list1 is list2)  # True
print(list1 is list3)  # False

# ---------- 동등성 비교 ----------
print(list1 == list2)  # True
print(list1 == list3)  # True
