#
#  완주하지 못한 선수.py
#  algorithm
#
#  Created by Kihun SONG on 2022/03/16.
#

def solution(participant, completion):
	participant.sort()
	completion.sort()

	for i in range(len(completion)):
		if completion[i] != participant[i]:
			return participant[i]

	return participant[-1]
