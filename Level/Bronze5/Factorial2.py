Num = int(input())

result = 1

if Num == 0:
    print("1")
else:
    for i in range(Num):
        result = result * Num
        Num = Num - 1

    print(result)