import sys


input = lambda: sys.stdin.readline().rstrip()

# 먼저 입력을 받아서 중복을 제거
n = int(input())
words = set()  # set으로 중복을 자동 제거하면서 단어들을 저장

for _ in range(n):
    word = input()
    words.add(word)

# 이제 정렬을 해야 하는데, set은 정렬이 안 되니까 리스트로 변환
# 길이 먼저, 그 다음 사전순으로 정렬
word_list = list(words)
word_list.sort(key=lambda x: (len(x), x))

# 정렬된 결과를 출력
for word in word_list:
    print(word)
