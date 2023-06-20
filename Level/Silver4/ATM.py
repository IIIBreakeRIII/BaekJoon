# No. 11399 ATM

num = int(input())
atm_time = list(map(int, input().split()))

atm_time.sort()

total_time = 0

for i in range(num):
    temp_time = 0
    if i == 0:
        total_time = total_time + atm_time[0]
    else:
        for j in range(i+1):
            temp_time = temp_time + atm_time[j]
        total_time = total_time + temp_time

print(total_time)
