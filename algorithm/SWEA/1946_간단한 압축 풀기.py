#
#  간단한 압축 풀기.py
#  algorithm
#
#  Created by Kihun SONG on 2022/07/01.
#

T = int(input())

for test_case in range(1, T + 1):
	N = int(input())
	s = ''
	for n in range(1, N + 1):
		Ci, Ki = input().split()
		Ki = int(Ki)
		for i in range(Ki):
			s += Ci

	print("#{}".format(test_case))

	count = 1
	for c in s:
		print(c, end= "")
		if count % 10 == 0:
			print()
		count += 1

	print()
