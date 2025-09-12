import sys


input = lambda: sys.stdin.readline().rstrip()

N = int(input())
N_arr = list(map(int, input().split()))

M = int(input())
M_arr = tuple(map(int, input().split()))


def binary_search(num, lp, rp):
    if rp < lp:
        return 0

    cp = (lp + rp) // 2

    if N_arr[cp] == num:
        return 1
    elif N_arr[cp] < num:
        return binary_search(num, cp + 1, rp)
    else:
        return binary_search(num, lp, cp - 1)


ans = []
N_arr.sort()
for i in range(M):
    ans.append(binary_search(M_arr[i], 0, N - 1))

for a in ans:
    print(a)
