H, M = input().split()
H = int(H)
M = int(M)
T = int(input())

if 60 - M > T:
  H = H
  M = M + T
  print(H, M)
elif 60 - M == T:
  H = H + 1
  M = 0
  print(H, M)
else:
  print("11")
  if T - (60 - M) > T:
    print("22")
    if T < 60:
      print("33")
      H = H + 1
      M = T - M
      print(H, M)
    else:
      M_H = int(M // 60)
      M_M = int(M % 60)
      if 60 - M_M > M:
        H = H + M_H
        M = M + M_M
        print(H, M)
      elif 60 - M_M == M:
        H = H + M_H + 1
        M = 0
        print(H, M)
      elif 60 - M_M < M:
        H = H + M_H + 1
        M = M - M_M
        print(H, M)