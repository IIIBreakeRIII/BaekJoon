String = input()
Alphabet = "abcdefghijklmnopqrstuvwxyz"

for i in Alphabet:
  if i in String:
    print(String.index(i), end = " ")
  else:
    print(-1, end = " ")