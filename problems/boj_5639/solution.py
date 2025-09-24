import sys

sys.setrecursionlimit(10**9)
lines = sys.stdin.read().strip().split("\n")
tree = list(map(int, lines))


def post_order(start, end):
    if start > end:
        return

    root = tree[start]  # 트리의 루트
    right_start = end + 1  # 트리의 마지막 리프
    for i in range(start + 1, end + 1):
        """오른쪽 서브 트리 찾기"""
        if tree[i] > root:  # 더 크면 여기서부터 오른쪽 트리? 노드?
            right_start = i
            break

    post_order(start + 1, right_start - 1)  # 왼쪽 트리 후위 순회
    post_order(right_start, end)  # 오른쪽 트리 후위 순회
    print(root)


post_order(0, len(tree) - 1)
