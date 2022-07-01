#
#  중간값 찾기.py
#  algorithm
#
#  Created by Kihun SONG on 2022/07/01.
#

n = int(input())
value = list(map(int, input().split()))
value.sort()
index = (n - 1) / 2
print("{0}".format(value[index]))

