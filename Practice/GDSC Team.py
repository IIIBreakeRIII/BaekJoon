import random

Member = ['Jonny', 'Paul', 'Ashton', 'Luna', 'Gom', 'Jinny',
'Jin', 'Blu', 'Yeon', 'Judy', 'Ethan', 'Maverick', 'Joel', 'Beom', 
'Ignacio', 'Philip', 'Neil', 'Harry', 'Sean', 'Bey', 'Hoon', 
'Gregorious', 'Jun', 'Tom', 'Woody', 'Cindy']

while True:
  print("Enter the name who does not attend :", end=' ')
  nonattendance = input()
  if nonattendance == "None" or nonattendance == "0":
    break
  else:
    Member.remove(nonattendance)

print("How many teams you will divide? : ", end='')
TeamCount = int(input())

TeamMemberCount = len(Member) // TeamCount

for i in range(TeamCount):

  if TeamMemberCount >= 0:
    temp = random.sample(Member, TeamMemberCount)
    print(i + 1, "Team :", temp)

    for j in range(len(temp)):
      Member.remove(temp[j])

    if len(Member) < TeamMemberCount:
      print(TeamCount + 1, "Team :", Member)
    else:
      continue