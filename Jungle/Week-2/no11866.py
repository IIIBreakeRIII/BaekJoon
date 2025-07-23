# No.11866 요세푸스 문제 0

from collections import deque

n, k = map(int, input().split())

deq = deque([i for i in range(1, n+1)])
result = []

while len(deq) != 0:

    for _ in range(k-1):
        deq.append(deq.popleft())

    result.append(str(deq.popleft()))

print('<'+', '.join(result)+'>')
