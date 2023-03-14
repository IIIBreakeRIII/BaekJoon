# No. 1312 소수

A, B, N = map(int, input().split())

for i in range(N):
	A = (A % B) * 10

Result = A // B

print(Result)
