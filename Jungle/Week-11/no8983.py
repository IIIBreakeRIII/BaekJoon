import sys
input = sys.stdin.readline

# 사대의 수, 동물의 수, 사정거리
M, N, L = map(int, input().split())
# 사대의 좌표 입력
saro = list(map(int, input().split()))
# 동물의 좌표
animal = [list(map(int, input().split())) for i in range(N)]

saro.sort()
count = 0

for a, b in animal:
    # 동물 좌표 b가 L보다 크다면, 잡을 수 없음
    if b > L:
        continue

    start = 0
    end = len(saro) - 1
    
    # 동물을 잡을수있는 최소값, 최대값
    Min = a + b - L
    Max = a - b + L

    while start <= end:
        mid = (start + end) // 2
        # 동물을 잡을 수 있다면, count += 1
        if Min <= saro[mid] <= Max:
            count += 1
            break
        elif saro[mid] < Max:   # 동물을 못잡고 Max보다 작을떄
            start = mid + 1
        else:
            end = mid - 1

print(count)
