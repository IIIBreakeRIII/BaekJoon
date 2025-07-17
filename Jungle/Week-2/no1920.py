# No.1920 수 찾기
# set 자료형 활용

n = int(input())
n_list = set(map(int, input().split()))

m = int(input())
m_list = list(map(int, input().split()))

for i in m_list:
    if i in n_list:
        print(1)
    else:
        print(0)

