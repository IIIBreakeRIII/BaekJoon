SpeedLimit = int(input())
ContinuousSpeed = int(input())

if ContinuousSpeed - SpeedLimit <= 0:
  print("Congratulations, you are within the speed limit!")
elif ContinuousSpeed - SpeedLimit > 0 and ContinuousSpeed - SpeedLimit <= 20:
  print("You are speeding and your fine is $100.")
elif ContinuousSpeed - SpeedLimit >= 21 and ContinuousSpeed - SpeedLimit <= 30:
  print("You are speeding and your fine is $270.")
elif ContinuousSpeed - SpeedLimit >= 31:
  print("You are speeding and your fine is $500.")