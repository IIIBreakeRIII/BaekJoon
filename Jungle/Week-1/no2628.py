# 종이자르기

w, h = map(int, input().split())

count = int(input())

w_list = [0]
h_list = [0]
square_list = []

for _ in range(count):
    i, j = map(int, input().split())
    
    if i == 0:
        h_list.append(j)
    else:
        w_list.append(j)

w_list.append(w)
h_list.append(h)

w_list.sort()
h_list.sort()

for i in range(1, len(w_list), 1):
    for j in range(1, len(h_list), 1):
        square_list.append((w_list[i] - w_list[i - 1]) * (h_list[j] - h_list[j-1]))

print(max(square_list))
