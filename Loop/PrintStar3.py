# No. 2444 별 찍기 - 7

num = int(input())
temp = 1

for i in range(1, num * 2):
    if i == num * 2:
        break
    elif i == num:
        print("*" * (num * 2 - 1))
    elif i < num:
        print(" " * (num - i) + "*" * (i * 2 - 1))
    elif i > num:
        index = i - (2 * temp)
        print(" " * (i - num) + "*" * (index * 2 - 1))
        temp = temp + 1
