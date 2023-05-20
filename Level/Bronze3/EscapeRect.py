# No. 1085 직사각형에서 탈출

x, y, w, h = map(int, input().split())
distance = []

distance.append(x)
distance.append(y)
distance.append(w - x)
distance.append(h - y)
distance.sort()

print(distance[0])
