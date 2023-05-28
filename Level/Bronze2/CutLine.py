# No. 25305 커트라인

N, K = map(int, input().split())
score_list = list(map(int, input().split()))

score_list.sort(reverse=True)

print(score_list[K-1])
