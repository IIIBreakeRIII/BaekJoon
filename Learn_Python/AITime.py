H, M, S = map(int, input().split())
T = int(input())
TS = T % 60
TT = T // 60
TM = TT % 60
TH = TT // 60

print(TM)
print(TH)

H += TH
M += TM
S += TS

if S >= 60:
  M += 1
  S -= 60
if M >= 60:
  H += 1
  M -= 60
if H >= 24:
  H -= 24
print(H, M, S)