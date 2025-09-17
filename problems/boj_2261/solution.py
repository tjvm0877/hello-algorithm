import sys

input = lambda: sys.stdin.readline().rstrip()


# 두 점 a, b 사이의 거리의 제곱을 계산하는 함수
def dist_sq(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


# 점이 3개 이하일 때는 모든 점 쌍을 비교하는 브루트포스 함수
def brute_force(points, left, right):
    min_d = float("inf")
    # 모든 점 쌍 비교
    for i in range(left, right):
        for j in range(i + 1, right):
            min_d = min(min_d, dist_sq(points[i], points[j]))
    return min_d


# 분할선 근처의 점들(Strip)을 이용해 최소 거리 찾기
def closest_strip(strip, d):
    # y좌표 기준으로 정렬을 해야 효과적으로 거리 비교 가능
    strip.sort(key=lambda x: x[1])
    min_d = d
    for i in range(len(strip)):
        # 현재 점 이후 최대 7개 점만 비교 (기하학적 성질)
        for j in range(i + 1, len(strip)):
            # y좌표 차이가 d보다 크면 이후 점들과의 거리도 클 수밖에 없으므로 중단
            if (strip[j][1] - strip[i][1]) ** 2 >= min_d:
                break
            min_d = min(min_d, dist_sq(strip[i], strip[j]))
    return min_d


# 분할 정복으로 최소 거리 계산 함수
def closest_pair(points, left, right):
    # 점의 수가 3개 이하인 영역은 브루트포스로 계산
    if right - left <= 3:
        return brute_force(points, left, right)

    mid = (left + right) // 2  # 중간 인덱스
    mid_x = points[mid][0]  # 중간 점의 x좌표 (분할 기준)

    # 왼쪽 절반 최근접 거리
    dl = closest_pair(points, left, mid)
    # 오른쪽 절반 최근접 거리
    dr = closest_pair(points, mid, right)
    # 왼쪽과 오른쪽 중 작은 거리
    d = min(dl, dr)

    # 분할선 기준 d 거리 내 점들만 모은 strip 생성
    strip = []
    for i in range(left, right):
        if (points[i][0] - mid_x) ** 2 < d:
            strip.append(points[i])

    # strip 내의 점들끼리만 비교해서 d 이하로 더 가까운 점 쌍 찾기
    ds = closest_strip(strip, d)

    # 전체 영역에서의 최소 거리 반환
    return min(d, ds)


n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# x좌표 기준으로 전체 점 정렬: 분할 기준이 x축 좌표임
points.sort(key=lambda x: x[0])

# 결과 출력: 최소 거리의 제곱
print(closest_pair(points, 0, n))
