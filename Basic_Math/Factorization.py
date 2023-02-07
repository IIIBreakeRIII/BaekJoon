# No. 11653 소인수분해

N = int(input())
FactorizeNum = 2

while(True):
    if N % FactorizeNum == 0:
        print(FactorizeNum)
        N = N // FactorizeNum
    elif N % FactorizeNum != 0:
        if FactorizeNum > N:
            break
        else:
            FactorizeNum = FactorizeNum + 1
            for i in range(FactorizeNum):
                if i == 0:
                    continue
                else:
                    if FactorizeNum % i == 0:
                        break
