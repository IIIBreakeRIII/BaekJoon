for i in range(3):
  WorkH, WorkM, WorkS, HomeH, HomeM, HomeS = map(int, input().split())
  WorkTime = (WorkH * 3600) + (WorkM * 60) + (WorkS)
  HomeTime = (HomeH * 3600) + (HomeM * 60) + (HomeS)
  
  Time = HomeTime - WorkTime

  Hour = Time // 3600
  Minute = (Time % 3600) // 60
  Seconds = (Time % 3600) % 60

  print(Hour, Minute, Seconds)