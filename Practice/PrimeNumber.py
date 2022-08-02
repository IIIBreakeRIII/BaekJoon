a = int(input())
b = int(input())
count = 0

for i in range(a, b+1):
    for j in range(2, b + 1):     
        if j == i:
            count += 1
        elif i % j == 0:
            break

print(count)