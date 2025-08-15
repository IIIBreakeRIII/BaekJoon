# No.1065 한수

import sys
input = sys.stdin.readline

n = int(input())

if n < 100:
    print(n)
else:
    count = 99
    
    for i in range(100, n + 1, 1):
        num_list = list(map(int, str(i)))
        
        if int(num_list[2]) - int(num_list[1]) == int(num_list[1]) - int(num_list[0]):
            count += 1

    print(count)
