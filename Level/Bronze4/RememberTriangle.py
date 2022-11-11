A = int(input())
B = int(input())
C = int(input())

Sum = A + B + C

if Sum != 180:
  print("Error")
else:
  if A == B == C == 60:
    print("Equilateral")
  elif A != B and A != C and B != C:
    print("Scalene")
  elif A == B or A == C or B == C:
    print("Isosceles")