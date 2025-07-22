# No.10773 제로

count = int(input())

money_list = []

for _ in range(count):
    temp = int(input())

    if temp == 0:
        if len(money_list) == 0:
            pass
        else:
            money_list.pop()
    else:
        money_list.append(temp)

print(sum(money_list))
