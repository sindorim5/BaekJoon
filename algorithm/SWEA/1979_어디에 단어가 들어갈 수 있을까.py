#
#  어디에 단어가 들어갈 수 있을까.py
#  algorithm
#
#  Created by Kihun SONG on 2022/07/01.
#

T = int(input())

for test_case in range(1, T+1):
	result = 0
	N, K = map(int, input().split())
	matrix = []
	for i in range(N):
		matrix.append(list(map(int, input().split())))

	for y in range(N):
		count = 0
		for x in range(N):
			if matrix[y][x] == 0:
				if count == K:
					result += 1
				count = 0
			else:
				count += 1
		if count == K:
			result += 1

	for x in range(N):
		count = 0
		for y in range(N):
			if matrix[y][x] == 0:
				if count == K:
					result += 1
				count = 0
			else:
				count += 1
		if count == K:
			result += 1

	print("#{0} {1}".format(test_case, result))
