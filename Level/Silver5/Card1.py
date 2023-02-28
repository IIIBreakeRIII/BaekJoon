# No. 2161 카드1

Num = int(input())
NumList1 = []
NumList2 = []
NumListTemp = []
temp = 0

for i in range(1, Num + 1):
    NumList1.append(i)

while True:
    if len(NumList1) == 1:
        break
    elif temp % 2 == 0:
        NumList2.append(NumList1[0])
        del NumList1[0]
        temp = temp + 1
    elif temp % 2 == 1:
        NumListTemp.append(NumList1[0])
        del NumList1[0]
        NumList1.append(NumListTemp[0])
        NumListTemp.clear()
        temp = temp + 1

NumList2.append(NumList1[0])

for k in range(len(NumList2)):
    print(NumList2[k], end=" ")

# 첫 코드

# for j in range(len(NumList1)):
#    if j % 2 == 0:
#        NumList2.append(NumList1[j])
#    else:
#        NumListTemp.append(NumList1[j])
#        NumList1.remove(j)
#        NumList1.append(NumListTemp[0])
#        NumListTemp.clear()
