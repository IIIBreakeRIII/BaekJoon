import sys

N, P, Q = map(int, input().split())
dict = {0:1}

# 반복문으로 돌렸을 때
# 시간 초과
for i in range(N + 1):
    if i == 0:
        pass
    else:
        result = dict[i // P] + dict[i // Q]
        dict[i] = result
        result = 0
 
if N == 0:
    print(1)
else:
    print(dict[N])

print()
print(sys.getsizeof(dict) / 10 ** 6, end="")
print("MB")
