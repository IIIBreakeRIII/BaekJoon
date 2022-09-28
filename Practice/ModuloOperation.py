M = int(input("Enter M : "))
ed = int(input("Enter ed : "))
n = int(input("Enter n : "))

NewM = M ** ed
result = NewM % n

print("M to the ed mod n = ", result)