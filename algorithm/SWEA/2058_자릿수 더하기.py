#
#  자릿수 더하기.py
#  algorithm
#
#  Created by Kihun SONG on 2022/07/01.
#

n = int(input())

result = 0

while n != 0:
	result += n % 10
	n = n // 10

print(result)
