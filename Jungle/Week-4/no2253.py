# No.2253 점프

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dp = [[float('inf')] * (int((2 * N)** 0.5) + 2) for _ in range(N + 1)] 
dp[1][0] = 0

stone_set = set()
for _ in range(M):
    stone_set.add(int(input()))

for i in range(2, N + 1):
    if i in stone_set:
        continue

    for j in range(1, int((2 * i) ** 0.5) + 1):
        dp[i][j] = min(dp[i - j][j - 1], dp[i - j][j], dp[i - j][j + 1]) + 1

if min(dp[N]) == float('inf'):
    print(-1)
else:
    print(min(dp[N]))

# import sys
# input = sys.stdin.readline
# 
# n, m = map(int, input().split())
# rock_list = [0 for _ in range(0, n)]
# 
# for _ in range(m):
#     rock_list[int(input()) - 1] = -1
# 
# jump = 1
# # 결과값
# count = 0
# 
# # 포인터 => indexing 해주는 애
# # current_location = 0
# 
# def check_jump(prev_jump, current_index):
# 
#     if rock_list[current_index + (prev_jump + 1)] == -1:
#         if rock_list[current_index + prev_jump] == -1:
#             if rock_list[current_index + (prev_jump - 1)] == -1:
#                 return -1
#             else:
#                 return current_index + (prev_jump - 1)
#         else:
#             return current_index + prev_jump
#     else:
#         return current_index + (prev_jump + 1)
# 
# init_index = 1
# 
# while True:
#     
#     if rock_list[1] == -1:
#         print(-1)
#         break
# 
#     count += 1
#     
#     current_index = check_jump(jump, init_index)
# 
#     jump = current_index - init_index
#     init_index = current_index
# 
#     if init_index >= n - 1:
#         print(count)
#         break
