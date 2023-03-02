# No. 3049 다각형의 대각선

# 다각형의 대각선 꼭짓점 개수 = nC4

num = int(input())
print(num * (num - 1) * (num - 2) * (num - 3) // 24)
