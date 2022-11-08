Info1, Math1, Sci1, Eng1 = map(int, input().split())
Info2, Math2, Sci2, Eng2 = map(int, input().split())

A = Info1 + Math1 + Sci1 + Eng1
B = Info2 + Math2 + Sci2 + Eng2

if A >= B:
  print(A)
else:
  print(B)