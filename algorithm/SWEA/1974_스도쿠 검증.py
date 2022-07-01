#
#  스도쿠 검증.py
#  algorithm
#
#  Created by Kihun SONG on 2022/07/01.
#

import sys

sys.stdin = open("input.txt", "r")

T = int(input())

check_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}

for test_case in range(1, T+1):
	matrix = []
	check = 0
	for i in range(9):
		matrix.append(list(map(int, input().split())))

	check_a = 1
	for y in range(0, 9, 3):
		a = 1
		for x in range(0, 9, 3):
			temp = set()
			for dy in range(3):
				for dx in range(3):
					temp.add(matrix[y + dy][x + dx])
			if temp == check_set:
				a = 1
			else:
				a = 0
			check_a *= a
		if check_a == 0:
			break

	check_b = 1
	for y in range(9):
		temp = set()
		for x in range(9):
			temp.add(matrix[y][x])
		if temp == check_set:
			check_b = 1
		else:
			check_b = 0
			break

	check_c = 1
	for x in range(9):
		temp = set()
		for y in range(9):
			temp.add(matrix[y][x])
		if temp == check_set:
			check_c = 1
		else:
			check_c = 0
			break

	check = check_a * check_b * check_c
	if check == 1:
		print("#{0} {1}".format(test_case, 1))
	else:
		print("#{0} {1}".format(test_case, 0))
