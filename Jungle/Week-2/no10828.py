# No.10828 스택

import sys
input = sys.stdin.readline

def push(list, num):
    list.append(num)
    return list

def pop(list):
    if len(list) == 0:
        print(-1)
        return list
    else:
        print(list.pop())
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

def top(list):
    if len(list) == 0:
        print(-1)
        return
    else:
        print(list[len(list) - 1])
        return list[len(list) - 1]

cmd_count = int(input())
stack = []

for _ in range(cmd_count):
    cmd = input().rstrip()

    if cmd[:4] == "push":
        push(stack, int(cmd[5:]))
    elif cmd == "top":
        top(stack)
    elif cmd == "size":
        size(stack)
    elif cmd == "empty":
        empty(stack)
    else:
        pop(stack)
