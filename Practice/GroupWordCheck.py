# No. 1316 그룹 단어 체커

TestCase = int(input())
count = 0

for i in range(TestCase):
  string = list(input())
  for j in range(len(string)):
    repeat = len(string) - j
    for k in range(len(string) - repeat):
      if string[j] == string[k + 1]:
        if j == k:
          continue
        else:
          count += 1

print(count)