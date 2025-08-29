# No.2110 공유기 설치

import sys
input = sys.stdin.readline

N, C = map(int, input().split())
pos = sorted(int(input()) for _ in range(N))

"""
최소 간격을 dist이상으로 유지
공유기 C개 이상 설치 가능 == True 조건
가장 왼쪽에 먼저 설치, 매번 dist만큼 떨어진 공간에 설치
"""
def can_place(dist):

    # 첫 집에 설치
    count = 1
    # 마지막으로 설치한 위치
    last = pos[0]
    
    for x in pos[1:]:
        # dist이상 떨어졌다면 설치 & last 최신화
        if x - last >= dist:
            count += 1
            last = x
            # 이미 C개를 채웠다면 True 반환
            if count >= C:
                return True
    
    return False

# 범위 설정
low, high = 1, pos[-1] - pos[0]
answer = 0

# upper-bound 까지 확인
while low <= high:
    mid = (low + high) // 2

    if can_place(mid):
        answer = mid
        low = mid + 1
    else:
        high = mid - 1

print(answer)
