#
#  폰켓몬.py
#  algorithm
#
#  Created by Kihun SONG on 2022/03/16.
#

def solution(nums):
    n = len(nums)
    halfN = len(nums) / 2
    setNums = set(nums)

    if len(setNums) >= halfN:
        return int(halfN)
    else:
        return len(setNums)
