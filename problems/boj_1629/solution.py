def mod_exp(A, B, C):
    if B == 0:
        return 1
    half = mod_exp(A, B // 2, C)
    half = (half * half) % C

    if B % 2 == 1:  # B가 홀수면 A 추가 곱하기
        half = (half * A) % C
    return half


A, B, C = map(int, input().split())
print(mod_exp(A, B, C))
