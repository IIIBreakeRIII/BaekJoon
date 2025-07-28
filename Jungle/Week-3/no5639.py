# No.5639 이진 검색 트리

import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

tree = []

while True:
    try:
        tree.append(int(input()))
    except:
        break

def postorder(start, end):
    if start >= end:
        return
    
    root = tree[start]
    idx = start + 1
    
    while idx < end and tree[idx] < root:
        idx += 1

    postorder(start + 1, idx)
    postorder(idx, end)
    print(root)

postorder(0, len(tree))
