# No. 1193 분수 찾기

Num = int(input())

count = 2

FirstNum = 1
SecondNum = 2

while True:
  if Num == FirstNum:
    print("1/1")
    break
  elif Num >= SecondNum and Num < SecondNum + count:
    NewNum = Num - (SecondNum - 1)    # Big Index = count, Samll Index = NewNum
    if count % 2 == 0:
      Numerator = count - (count - NewNum)    # 분자
      Denominator = count - NewNum + 1        # 분모
      print("{}/{}".format(Numerator, Denominator))
    else:
      Numerator = count - NewNum + 1
      Denominator = count - (count - NewNum)
      print("{}/{}".format(Numerator, Denominator))
    break
  else:
    SecondNum = SecondNum + count     # Index value
    count = count + 1                 # Add value