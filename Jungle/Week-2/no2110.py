# No.2110 공유기 설치

import sys
input = sys.stdin.readline

house, router = map(int, input().split())
house_list = []

for _ in range(house):
    house_list.append(int(input().rstrip()))

house_list.sort()

def search(array, start, end):
    while start <= end:
        mid = (start + end) // 2
        current = array[0]
        count = 1

        for i in range(1, len(array)):
            if array[i] >= current + mid:
                count += 1
                current = array[i]

        if count >= router:
            global answer
            start = mid + 1
            answer = mid
        else:
            end = mid - 1

start = 1
end = house_list[-1] - house_list[0]
answer = 0

search(house_list, start, end)
print(answer)
