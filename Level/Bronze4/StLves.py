while True:
  
  A = float(input())

  if A == 0:
    break
  else:
    Result = A + A ** 2 + A ** 3 + A ** 4 + 1
    print("%.2f" % Result)