from math import inf
import sys


input = lambda: sys.stdin.readline().rstrip()


def get_max(i, visited, selected):
    global numbers

    if i >= len(visited):
        sum = 0
        for index in range(1, i):
            sum += abs(selected[index - 1] - selected[index])
        return sum

    ans = float(-inf)
    for num in range(len(visited)):
        if visited[num] == True:
            continue
        visited[num] = True
        ans = max(ans, get_max(i + 1, visited, selected + [numbers[num]]))
        visited[num] = False

    return ans


n = int(input())
numbers = list(map(int, input().split()))
visited = [False] * n

print(get_max(0, visited, list()))
