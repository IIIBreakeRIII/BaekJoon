# No. 1259 팰린드롬수

while True:
    A = int(input())
    if A == 0:
        break
    else:
        list_A = list(map(int, str(A)))
        temp_j = len(list_A) - 1
        temp_list = []
        for _ in range(len(list_A)):
            temp_list.append(list_A[temp_j])
            temp_j = temp_j - 1
        if list_A == temp_list:
            print("yes")
        else:
            print("no")
