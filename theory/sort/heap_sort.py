def heapify(arr, n, i):
    largest = i  # 루트 노드
    left = 2 * i + 1  # 왼쪽 자식
    right = 2 * i + 2  # 오른쪽 자식

    # 왼쪽 자식이 루트보다 크면 largest 변경
    if left < n and arr[left] > arr[largest]:
        largest = left

    # 오른쪽 자식이 현재 largest보다 크면 largest 변경
    if right < n and arr[right] > arr[largest]:
        largest = right

    # largest가 루트가 아니면 교체 후 재귀 호출
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # 배열을 최대 힙으로 변환
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # 힙에서 하나씩 요소를 꺼내 정렬
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # 루트와 마지막 요소를 교체
        heapify(arr, i, 0)  # 힙 구조 유지


if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    heap_sort(arr)
    print(arr)
