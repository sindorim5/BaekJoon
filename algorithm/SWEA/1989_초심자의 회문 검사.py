#
#  초심자의 회문 검사.py
#  algorithm
#
#  Created by Kihun SONG on 2022/07/01.
#

import sys

T = int(input())

for t in range(1, T + 1):
	s = input()
	if s == s[::-1]:
		print("#{0} {1}".format(t, 1))
	else:
		print("#{0} {1}".format(t, 0))

