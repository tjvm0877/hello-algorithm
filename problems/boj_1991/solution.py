import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
tree = {}
for _ in range(N):
    node, left, right = input().split()
    tree[node] = [left, right]


# 전위순회 (Preorder Traversal)
#   순서: 루트 → 왼쪽 자식 → 오른쪽 자식
#   목적: 트리의 구조를 그대로 표현하거나 복제할 때 유용
#   활용: 트리를 직렬화하거나, 루트 노드를 먼저 처리하는 재귀적 문제 해결에 적합. 파일 시스템 디렉토리 탐색 시에도 주로 사용
def preorder(node):
    if node != ".":
        print(node, end="")
        preorder(tree[node][0])
        preorder(tree[node][1])


# 중위순회 (Inorder Traversal)
#   순서: 왼쪽 자식 → 루트 → 오른쪽 자식
#   목적: 이진 탐색 트리에서 노드 값을 오름차순으로 정렬하여 출력할 때 주로 사용
#   활용: 값을 정렬해서 순차적으로 처리해야 할 때 적합하며, 트리 내 값의 순서를 알고 싶을 때 사용
def inorder(node):
    if node != ".":
        inorder(tree[node][0])
        print(node, end="")
        inorder(tree[node][1])


# 후위순회 (Postorder Traversal)
#   순서: 왼쪽 자식 → 오른쪽 자식 → 루트
#   목적: 자식 노드를 모두 처리한 후에 부모 노드를 처리해야 할 때 유용
#   활용: 트리 삭제, 메모리 해제, 구조를 아래서부터 처리하는 작업에 적합. 컴퓨터 시스템에서 디렉토리 구조 삭제 등에서 사용
def postorder(node):
    if node != ".":
        postorder(tree[node][0])
        postorder(tree[node][1])
        print(node, end="")


# 위 규칙은 사실 이진 탐색 트리일 때의 이야기
#   일반적인 이진트리도 전위순회, 중위순회, 후위순회 방법은 동일하게 적용
#   다만, 이진 탐색 트리(BST)와 달리 중위순회가 반드시 정렬된 순서로 노드를 방문하는 것을 보장하지 않음

# 그냥 이진 트리의 경우
# 전위순회: 트리 구조를 재귀적으로 처리하거나 복제할 때 유용
# 중위순회: 이진 탐색 트리가 아니면 방문 순서가 정렬 순서와 일치하지 않을 수 있음. 대신 트리의 구조적인 특성을 이해하거나, 수식 트리와 같은 표현에 활용
# 후위순회: 자식 노드들을 모두 처리한 뒤 부모 노드를 처리하는 용도로 사용, 예를 들어 트리 삭제나 후위 계산(수식 트리 평가 등)에 적합

preorder("A")
print()
inorder("A")
print()
postorder("A")
