#
#  두 개의 숫자열.py
#  algorithm
#
#  Created by Kihun SONG on 2022/07/01.
#

T = int(input())

for test_case in range(1, T+1):
	N, M = map(int, input().split())
	A = list(map(int, input().split()))
	B = list(map(int, input().split()))

	if N > M:
		N, M = M, N
		A, B = B, A

	max = 0

	for i in range(M - N + 1):
		sum = 0
		for j in range(N):
			sum += A[j] * B[i+j]
		if sum > max:
			max = sum

	print("#{0} {1}".format(test_case, max))
