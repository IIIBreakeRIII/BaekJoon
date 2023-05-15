# No. 1037 약수

N = int(input())
divisor_list = list(map(int, input().split()))

divisor_list.sort()

if len(divisor_list) == 0:
    print(divisor_list[0] ** 2)
else:
    print(divisor_list[0] * divisor_list[len(divisor_list) - 1])
