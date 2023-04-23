# No. 18409 Counting Vowels

Num = int(input())
Word = list(input())
Vowels = ["a", "e", "i", "o", "u"]

cnt = 0
for i in range(len(Word)):
	for j in range(len(Vowels)):
		if Word[i] == Vowels[j]:
			cnt = cnt + 1
		else:
			continue

print(cnt)
