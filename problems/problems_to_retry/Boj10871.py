n, x = map(int, input().split())
arr = list(map(int, input().split()))

ans = list()
for num in arr:
    if num < x:
        ans.append(num)

for item in ans:
    print(item, end=' ')
