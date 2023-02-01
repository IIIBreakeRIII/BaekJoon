# No. 2775 부녀회장이 될테야
# 도전중

testcase = int(input())

for i in range(testcase):
  floor = int(input())                                  # 층
  num = int(input())                                    # 호
  PeopleCount = [i for i in range(1, num + 1)]          # 초기값은 0층, 호 수 별로 사람 수

  for j in range(floor):                                # 층 별로 확인
    NewPeopleCount = []                                 # 새로운 리스트 생성
    for k in range(num):                                # 해당 호수까지 합
      NewPeopleCount.append(sum(PeopleCount[:k+1]))     # 이전 층의 호수까지 합
    PeopleCount = NewPeopleCount                        # 새로 만들어진 리스트 NewPeopleCount를 이전 PeopleCount로 대체
  
  print(PeopleCount[-1])