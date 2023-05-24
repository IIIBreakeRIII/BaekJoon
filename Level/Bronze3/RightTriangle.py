# No. 4153 직각삼각형

while True:
    list_triangle = list(map(int, input().split()))
    if list_triangle[0] == list_triangle[1] == list_triangle[2] == 0:
        break
    else:
        list_triangle.sort(reverse=True)
        if list_triangle[0] ** 2 == list_triangle[1] ** 2 + list_triangle[2] ** 2:
            print("right")
        else:
            print("wrong")
