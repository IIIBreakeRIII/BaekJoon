print("Enter M : ")
M = int(input())
print("Enter ed : ")
ed = int(input())
print("Enter n : ")
n = int(input())

NewM = M ** ed
result = NewM % n

print("M to the ed mod n = ", result)