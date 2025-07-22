# No.9012 괄호

n = int(input())

for _ in range(n):
    bracket = input()

    bracket_list = []

    for index in bracket:
        if len(bracket_list) == 0:
            if index == ")":
                bracket_list.append(index)
                break
            else:
                bracket_list.append(index)
        elif index == bracket_list[len(bracket_list) - 1]:
            bracket_list.append(index)
        elif index != bracket_list[len(bracket_list) - 1]:
            
            bracket_list.pop()
    
    print("YES" if len(bracket_list) == 0 else "NO")
