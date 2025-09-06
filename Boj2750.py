n = int(input())

n_list = list()
for i in range(n):
    num = int(input())
    if len(n_list) == 0:
        n_list.append(num)
    else:
        for j in range(len(n_list)):
            if num < n_list[j]:
                n_list.insert(j, num)
                break
            elif j == len(n_list) - 1:
                n_list.append(num)

for num in n_list:
    print(num)
