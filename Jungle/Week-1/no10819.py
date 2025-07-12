# testcase = int(input())
# num_list = list(map(int, input().split()))
# 
# num_list.sort()
# 
# absolute_list = []
# 
# result = 0
# 
# small_list = num_list[:int(len(num_list) // 2)]
# big_list = num_list[int(len(num_list) // 2):]
# 
# if len(small_list) == len(big_list):
#     for i in range(len(small_list)):
#         absolute_list.append(big_list[i])
#         absolute_list.append(small_list[i])
# elif len(small_list) > len(big_list):
#     for i in range(len(big_list)):
#         absolute_list.append(small_list[i])
#         absolute_list.append(big_list[i])
#     absolute_list.append(small_list[len(small_list) - 1])
# else:
#     for i in range(len(small_list)):
#         absolute_list.append(big_list[i])
#         absolute_list.append(small_list[i])
#     absolute_list.append(big_list[len(big_list) - 1])
# 
# for i in range(len(absolute_list) - 1):
#     result += abs(absolute_list[i] - absolute_list[i + 1])
# 
# print(result)

from itertools import permutations

n = int(input())
num_list = list(map(int, input().split()))

ans = 0
for p in permutations(num_list):
    s = sum(abs(p[i] - p[i + 1]) for i in range(n-1))
    ans = max(ans, s)

print(ans)
