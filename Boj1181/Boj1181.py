import sys

n = int(sys.stdin.readline())
words = [sys.stdin.readline().strip() for i in range(n)]

# 람다 사용
# key_func = lambda x: (len(x), x)
# print(key_func("apple"))  # 출력: (5, 'apple')
words = list(set(words))  # set으로 바꿔서 중복 제거
words.sort(key=lambda x: (len(x), x))  # 길이+사전순 정렬

for word in words:
    print(word)
