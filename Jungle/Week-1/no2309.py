# 일곱 난쟁이

height = [int(input()) for _ in range(9)]
total = sum(height)
man_1 = man_2 = 0

for i in range(8):
    for j in range(i+1, 9):
        if height[i] + height[j] == total - 100:
            man_1, man_2 = height[i], height[j]
            break
    if man_1 is not 0:
        break

height.remove(man_1)
height.remove(man_2)
height.sort()

for h in height:
    print(h)
