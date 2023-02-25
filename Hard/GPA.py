# No. 25206 너의 평점은
# IndexError in Boj
# Solved

GPAList = []
GPASum = 0.000000
Sum = 0.000000

for i in range(20):
    GPAList.append(input().split())
    if GPAList[i][2] == "A+":
        GPAList[i][2] = "4.5"
    elif GPAList[i][2] == "A0":
        GPAList[i][2] = "4.0"
    elif GPAList[i][2] == "B+":
        GPAList[i][2] = "3.5"
    elif GPAList[i][2] == "B0":
        GPAList[i][2] = "3.0"
    elif GPAList[i][2] == "C+":
        GPAList[i][2] = "2.5"
    elif GPAList[i][2] == "C0":
        GPAList[i][2] = "2.0"
    elif GPAList[i][2] == "D+":
        GPAList[i][2] = "1.5"
    elif GPAList[i][2] == "D0":
        GPAList[i][2] = "1.0"
    elif GPAList[i][2] == "F":
        GPAList[i][2] = "0.0"
    elif GPAList[i][2] == "P":      # Pass 과목의 경우 remove 하지 말고 pass 하게 해야함 (조건에 20개이기 때문)
        continue

for j in range(len(GPAList)):
    if GPAList[j][2] == "P":
        continue
    else:
        GPASum = GPASum + float(GPAList[j][1])
        Sum = Sum + (float(GPAList[j][1]) * float(GPAList[j][2]))

GPA = Sum / GPASum
print(round(GPA, 6))
