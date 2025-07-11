A = int(input())
B = int(input())
C = int(input())

result = A * B * C
list_result = list(map(int, str(result)))

count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(len(list_result)):
    count[list_result[i]] = count[list_result[i]] + 1

for j in range(len(count)):
    print(count[j])
