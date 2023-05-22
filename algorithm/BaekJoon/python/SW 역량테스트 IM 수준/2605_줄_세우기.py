#
#  2605_줄_세우기.py
#  algorithm
#
#  Created by Kihun SONG on 2022/07/06.
#

# 5
# 0 1 1 3 2
# 4 2 5 3 1

count = int(input())
a = list(map(int, input().split()))
result = [1]

for i in range(1, count):
	result.insert(len(result) - a[i], i+1)

for i in result:
	print(i, end=" ")
