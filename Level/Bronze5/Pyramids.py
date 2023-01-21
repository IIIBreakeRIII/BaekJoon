# No. 5341 Pyramids

while True:
    num = int(input())
    if num == 0:
        break
    else:
        cnt = 1
        result = 0
        for i in range(num):
            result = cnt + result
            cnt = cnt + 1
        print(result)
