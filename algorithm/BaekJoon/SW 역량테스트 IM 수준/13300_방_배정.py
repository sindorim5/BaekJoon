#
#  13300_방_배정.py
#  algorithm
#
#  Created by Kihun SONG on 2022/07/06.
#

N, K = map(int, input().split())

girls = [0, 0, 0, 0, 0, 0]
boys = [0, 0, 0, 0, 0, 0]

count = 0

for i in range(N):
	gender, grade = map(int, input().split())

	if gender == 0:
		girls[grade - 1] += 1
	else:
		boys[grade - 1] += 1

for i in range(6):
	if girls[i] % K == 0:
		count = count + girls[i] // K
	else:
		count = count + girls[i] // K + 1

	if boys[i] % K == 0:
		count = count + boys[i] // K
	else:
		count = count + boys[i] // K + 1

print(count)
