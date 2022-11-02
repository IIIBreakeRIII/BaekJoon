while True:
  Name, Age, Weight = map(str, input().split())
  if Name == "#" and Age == "0" and Weight == "0":
    break
  if int(Age) > 17 or int(Weight) >= 80:
    print(Name, "Senior")
  else:
    print(Name, "Junior")