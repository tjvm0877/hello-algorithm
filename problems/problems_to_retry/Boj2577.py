a = int(input())
b = int(input())
c = int(input())

mul = a * b * c
mul_arr = list(map(int, str(mul)))
my_list = [0 for _ in range(10)]

for num in mul_arr:
    my_list[num] += 1

for ans in my_list:
    print(ans)
