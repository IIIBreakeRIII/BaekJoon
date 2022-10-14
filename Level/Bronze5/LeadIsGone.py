Lead = int(input())

BreakeR = 5
KillHim = Lead % BreakeR

if KillHim == 0:
  print(Lead // BreakeR)
else:
  print(Lead // BreakeR + 1)