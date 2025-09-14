import sys

input = lambda: sys.stdin.readline().rstrip()


# input: 동물의 x 위치
# output: 가장 가까운 사대의 위치
def get_closest_firing_lane(x, left, right):

    mid = (left + right) // 2

    # 구간이 두 칸 이하로 좁혀지면 직접 두 칸의 인덱스를 비교하여 더 가까운 사대를 반환하며 재귀를 멈춤
    # 사대가 항상 동물의 x축에 있지 않을 수 있기 때문
    if (right - left) == 1:
        a = abs(m_arr[right] - x)
        b = abs(m_arr[left] - x)
        return left if a > b else right
    elif right == left:
        return right
    elif m_arr[mid] < x:
        # m_arr[mid] < x인 경우: 동물보다 왼쪽에 있는 사대이지만, 이 사대가 가장 가까울 수도 있음
        return get_closest_firing_lane(x, mid, right)
    else:
        # m_arr[mid] >= x인 경우: 동물과 같거나 오른쪽에 있는 사대이지만, 역시 가장 가까울 수도 있음
        return get_closest_firing_lane(x, left, mid)


m, n, l = map(int, input().split())
m_arr = list(map(int, input().split()))
n_arr = tuple(tuple(map(int, input().split())) for _ in range(n))
m_arr.sort()

count = 0
for animal in n_arr:
    # 가장 가까운 사대를 찾는다.
    closest = get_closest_firing_lane(animal[0], 0, m - 1)

    # 사정거리가 되는지 체크하고 가능하다면 count를 증가시켜준다.
    if abs(m_arr[closest] - animal[0]) + animal[1] <= l:
        count += 1

# 결과를 반환한다.
print(count)
