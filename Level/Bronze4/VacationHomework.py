Vacation = int(input())
Math = int(input())
Language = int(input())
MaxMath = int(input())
MaxLanguage = int(input())

DuringMath = 0
DuringLanguage = 0

if Math % MaxMath != 0:
  DuringMath = Math // MaxMath + 1
else:
  DuringMath = Math // MaxMath

if Language % MaxLanguage != 0:
  DuringLanguage = Language // MaxLanguage + 1
else:
  DuringLanguage = Language // MaxLanguage

if DuringMath == DuringLanguage:
  print(Vacation - DuringMath)
elif DuringMath > DuringLanguage:
  print(Vacation - DuringMath)
else:
  print(Vacation - DuringLanguage)