# No. 11653 소인수분해
# 기존 코드 시간 초과

# 다음은 시간 초과 코드

# N = int(input())
# FactorizeNum = 2
# 
# while(True):
#     if N % FactorizeNum == 0:
#         print(FactorizeNum)
#         N = N // FactorizeNum
#     else:
#         if FactorizeNum > N:
#             break
#         else:
#             FactorizeNum = FactorizeNum + 1
#             for i in range(FactorizeNum):
#                 if i == 0:
#                     continue
#                 else:
#                     if FactorizeNum % i == 0:
#                         break

import time

N = int(input())
FactorizeNum = 2

start = time.time()

while(True):
    if N % FactorizeNum == 0:
        print(FactorizeNum)
        N = N // FactorizeNum
    else:
        if FactorizeNum > N:
            break
        else:
            FactorizeNum = FactorizeNum + 1
            for i in range(2, FactorizeNum):
                if FactorizeNum % i == 0:
                        break

end = time.time()

print(f"{end - start:.5f} seconds")
