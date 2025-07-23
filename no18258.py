# No.18258 큐 2

import sys
from collections import deque

input = sys.stdin.readline

def push(list, num):
    list.append(num)
    return list

def pop(list):
    if len(list) == 0:
        print(-1)
        return list
    else:
        print(list.popleft())
        return list

def size(list):
    print(len(list))
    return len(list)

def empty(list):
    if len(list) == 0:
        print(1)
        return 1
    else:
        print(0)
        return 0

def front(list):
    if len(list) == 0:
        print(-1)
        return
    else:
        print(list[0])

def back(list):
    if len(list) == 0:
        print(-1)
        return
    else:
        print(list[-1])

cmd_count = int(input())
queue = deque([])

for _ in range(cmd_count):
    cmd = input().rstrip()

    if cmd[:4] == "push":
        push(queue, int(cmd[5:]))
    elif cmd == "pop":
        pop(queue)
    elif cmd == "size":
        size(queue)
    elif cmd == "empty":
        empty(queue)
    elif cmd == "front":
        front(queue)
    else:
        back(queue)
