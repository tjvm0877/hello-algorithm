t = int(input())

for tc in range(t):
    input_str = input()
    input_arr = input_str.split()

    ans = ""
    for c in input_arr[1]:
        for l in range(int(input_arr[0])):
            ans += c
    print(ans)
