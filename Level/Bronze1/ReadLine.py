# No. 10798 세로 읽기

line1 = list(input())
line2 = list(input())
line3 = list(input())
line4 = list(input())
line5 = list(input())

line = [line1, line2, line3, line4, line5]

max_value = 0
for k in range(5):
    if len(line[k]) >= max_value:
        max_value = len(line[k])

for i in range(max_value):
    for j in range(5):
        try:
            print(line[j][i], end="")
        except IndexError as err:
            pass
