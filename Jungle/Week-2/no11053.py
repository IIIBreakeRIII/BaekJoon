# No.11053 가장 긴 증가하는 부분 수열

n = int(input())

num_list = list(map(int, input().split()))
result_list = [1] * n

for i in range(len(num_list)):
    for j in range(i):
        if num_list[i] > num_list[j]:
            result_list[i] = max(result_list[i], result_list[j] + 1)

print(max(result_list))
