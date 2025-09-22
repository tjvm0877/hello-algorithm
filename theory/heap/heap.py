import sys


class MinHeap:
    def __init__(self, items=[]):
        # 초기 리스트가 없으면 빈 리스트 사용
        self.heap = items if items is not None else []
        # 힙 조건을 만족하도록 리스트를 재구성
        if self.heap:
            self._build_heap()

    def _build_heap(self):
        # 힙의 중간 노드부터 루트까지 내려가며 힙 조건을 맞춤
        for i in reversed(range(len(self.heap) // 2)):
            self._heapify_down(i)

    def parent(self, index):
        # 현재 인덱스의 부모 노드 인덱스 계산 (완전 이진트리 특성)
        return (index - 1) // 2

    def left_child(self, index):
        # 현재 인덱스의 왼쪽 자식 노드 인덱스 계산
        return 2 * index + 1

    def right_child(self, index):
        # 현재 인덱스의 오른쪽 자식 노드 인덱스 계산
        return 2 * index + 2

    def swap(self, i, j):
        # 두 인덱스에 해당하는 힙 요소 위치 교환
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, key):
        # 힙의 끝에 새 키 추가
        self.heap.append(key)
        # 새로 추가된 노드가 힙 조건을 만족하도록 위로 올림
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        # 새로 추가된 노드가 부모 노드보다 작으면 위치 교환을 반복하는 과정
        while index > 0 and self.heap[self.parent(index)] > self.heap[index]:
            self.swap(index, self.parent(index))
            index = self.parent(index)  # 부모 노드 인덱스로 이동하여 조건 반복 검사

    def extract_min(self):
        # 힙이 비어있으면 예외
        if not self.heap:
            raise IndexError("extract_min from empty heap")
        # 루트 노드인 최소값 저장
        min_item = self.heap[0]
        # 힙 마지막 노드를 루트에 배치하고 리스트에서 마지막 노드 제거
        last_item = self.heap.pop()
        if self.heap:
            self.heap[0] = last_item
            # 루트 노드가 힙 조건을 만족하도록 아래로 내림
            self._heapify_down(0)
        return min_item

    def _heapify_down(self, index):
        # 루트 노드부터 자식 노드들과 비교하며 적절한 위치로 내려가는 과정
        smallest = index
        left = self.left_child(index)
        right = self.right_child(index)

        # 왼쪽 자식이 존재하고 현재 노드보다 작으면 위치 저장
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        # 오른쪽 자식이 존재하고 현재(왼쪽 자식과 비교 후) 노드보다 작으면 위치 저장
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        # 만약 자식 노드 중 더 작은 노드가 현재 노드라면 위치 교환 후 계속 재귀
        if smallest != index:
            self.swap(index, smallest)
            self._heapify_down(smallest)

    def peek_min(self):
        # 루트 노드인 최소값 반환 (힙이 비어있으면 예외)
        if not self.heap:
            raise IndexError("peek_min from empty heap")
        return self.heap[0]

    def is_empty(self):
        # 힙이 비어있는지 여부 반환
        return len(self.heap) == 0

    def size(self):
        # 힙에 저장된 요소 개수 반환
        return len(self.heap)


input = lambda: sys.stdin.readline().rstrip()

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

pq = MinHeap(arr)

result = 0
while pq.size() > 1:
    first = pq.extract_min()
    second = pq.extract_min()

    sum = first + second
    pq.insert(sum)
    result += sum

print(result)
