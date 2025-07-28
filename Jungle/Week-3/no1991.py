# No.1991 트리 순회

import sys
sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline

node_count = int(input())
node_dict = {}

for _ in range(node_count):
    parent, left, right = map(str, input().split())
    node_dict[parent] = [left, right]

# 전위 순회
def preorder(node):
    if node != ".":
        print(node, end="")
        preorder(node_dict[node][0])
        preorder(node_dict[node][1])

# 중위 순회
def inorder(node):
    if node != ".":
        inorder(node_dict[node][0])
        print(node, end="")
        inorder(node_dict[node][1])

# 후위 순회
def postorder(node):
    if node != ".":
        postorder(node_dict[node][0])
        postorder(node_dict[node][1])
        print(node, end="")

preorder("A")
print("")
inorder("A")
print("")
postorder("A")
