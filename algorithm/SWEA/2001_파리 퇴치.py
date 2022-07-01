#
#  파리 퇴치.py
#  algorithm
#
#  Created by Kihun SONG on 2022/07/01.
#

T = int(input())

for test_case in range(1, T+1):
	N, M = map(int,input().split())
	matrix = []
	for i in range(N):
		matrix.append(list(map(int, input().split())))

	max = 0

	for y in range(N - M + 1):
		for x in range(N - M + 1):
			fly = 0
			for dy in range(M):
				for dx in range(M):
					fly += matrix[y + dy][x + dx]
				if fly > max:
					max = fly

	print("#{0} {1}".format(test_case, max))

