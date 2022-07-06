#
#  숫자 배열 회전.py
#  algorithm
#
#  Created by Kihun SONG on 2022/07/01.
#

T = int(input())

for test_case in range(1, T+1):
	N = int(input())
	matrix = []
	for i in range(N):
		matrix.append(list(map(int, input().split())))

	matrix_90 = []
	matrix_180 = []
	matrix_270 = []

	for x in range(N):
		temp = []
		for y in reversed(range(N)):
			temp.append(matrix[y][x])
		matrix_90.append(temp)

	for y in reversed(range(N)):
		temp = []
		for x in reversed(range(N)):
			temp.append(matrix[y][x])
		matrix_180.append(temp)

	for x in reversed(range(N)):
		temp = []
		for y in range(N):
			temp.append(matrix[y][x])
		matrix_270.append(temp)

	print("#{0}".format(test_case))
	for i in range(N):
		print("".join(map(str, matrix_90[i])), end= " ")
		print("".join(map(str, matrix_180[i])), end= " ")
		print("".join(map(str, matrix_270[i])), end= " ")
		print()
