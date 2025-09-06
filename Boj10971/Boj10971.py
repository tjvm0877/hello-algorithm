import sys

n = int(sys.stdin.readline().strip())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

visited = [False] * n

# 순회 경로는 순환(cycle)이기 때문에 어느 도시에서 출발해도 최소 비용과 경로가 같음 (경로를 돌리는 것에 불과)
# 따라서 알고리즘 단순화를 위해 출발 도시를 0번으로 고정하고 탐색하며, 모든 도시를 방문한 후 다시 0번으로 돌아오는 것으로 계산함
# 출발 도시를 바꾸면 결과는 회전된 경로일 뿐, 최소 비용 값은 동일
start = 0  # 출발 도시 고정
visited[start] = True


def tsp(pos, count, cost):
    if count == n:
        if matrix[pos][start] != 0:
            return cost + matrix[pos][start]
        else:
            return float('inf')

    local_min = float('inf')  # local_min 초기화를 최댓값으로 설정
    for i in range(n):
        if not visited[i] and matrix[pos][i] != 0:
            visited[i] = True
            local_min = min(local_min, tsp(i, count + 1, cost + matrix[pos][i]))
            visited[i] = False
    return local_min


print(tsp(start, 1, 0))
