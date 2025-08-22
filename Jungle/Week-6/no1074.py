# No.1074 Z

import sys
input = sys.stdin.readline

num, row, col = map(int, input().split())
size = 2 ** num

def find_num(row, col, num, ans):

    num = num // 2
    
    # second quadrant
    if row < num and col < num:
        # breakpoint of recursion
        # if num == 1 i.e., if the 2x2 array, return the second quadrant
        if num == 1:
            print(ans)
            exit(0)
        find_num(row, col, num, ans)

    # first quadrant
    elif row < num and col >= num:
        if num == 1:
            print(ans + 1)
            exit(0)
        find_num(row, col - num, num, ans + num ** 2)

    # third quadrant
    elif row >= num and col < num:
        if num == 1:
            print(ans + 2)
            exit(0)
        find_num(row - num, col, num, ans + num ** 2 * 2)

    # fourth quadrant
    else:
        if num == 1:
            print(ans + 3)
            exit(0)
        find_num(row - num, col - num, num, ans + num**2 * 3)

find_num(row, col, size, 0)
