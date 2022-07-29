#
#  2330_일곱_난쟁이.py
#  algorithm
#
#  Created by Kihun SONG on 2022/07/06.
#

sum = 0
height = []

for _ in range(9):
	a = int(input())
	height.append(a)
	sum += a

for i in range(9):
	for j in range(i+1, 9):
		if sum - (height[i] + height[j]) == 100:
			a, b = height[i], height[j]

			height.remove(a)
			height.remove(b)
			height.sort()

			for i in height:
				print(i)
			break

	if len(height) < 9:
		break


