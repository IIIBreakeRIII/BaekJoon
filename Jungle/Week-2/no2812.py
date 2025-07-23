# No.2812 크게 만들기

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
numbers = input().rstrip()

stack = []

for num in numbers:
    # 스택이 비어있거나, 스택에 현재 마지막에 있는 원소가
    # number보다 작으면 pop, k 즉 앞에서부터 제거하는 경우를 1개 줄여줌
    # stack and stack[-1]을 해주는 이유는
    # stack이 비어있을 경우 stack이 비워져있다는 확인이 필요하기 때문
    # -1만 하면 IndexOutOfRange 남
    while stack and stack[-1] < num and k > 0:
        stack.pop()
        k -= 1
    stack.append(num)

if k > 0:
    print(''.join(stack[:-k]))
else:
    print(''.join(stack))
