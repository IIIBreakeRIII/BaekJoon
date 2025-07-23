#No.2164 카드2

import sys
from collections import deque

input = sys.stdin.readline

card_num = int(input())
card_deque = deque([i for i in range(1, card_num + 1)])

while len(card_deque) != 1:

    card_deque.popleft()
    temp = card_deque[0]
    card_deque.popleft()
    card_deque.append(temp)
    
print(*card_deque)
