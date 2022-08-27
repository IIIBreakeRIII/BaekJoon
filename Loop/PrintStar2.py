T = int(input())

for i in range(T):
  count_1 = i+1
  count_2 = T-i-1
  star = "*"
  blank = " "
  print(blank * count_2 + star * count_1)
