import sys

sys.stdin = open("input.txt", "r", encoding="utf-8")

w, h = map(int, input().split())
cvs = int(input())

#arr = [0 for _ in range(w*2 + h*2 - 2)]
cvsList = []
fullLength = w*2 + h*2
leftTop = 0
rightTop = w
leftBot = fullLength - h

for _ in range(cvs):
    direction, distance = map(int, input().split())
    if direction == 1:
        cvsLoc = leftTop + distance
    elif direction == 2:
        cvsLoc = leftBot - distance
    elif direction == 3:
        cvsLoc = fullLength - distance
    else:
        cvsLoc = rightTop + distance
    cvsList.append(cvsLoc)

myLoc = 0
direction, distance = map(int, input().split())
if direction == 1:
    myLoc = leftTop + distance
elif direction == 2:
    myLoc = leftBot - distance
elif direction == 3:
    myLoc = fullLength - distance
else:
    myLoc = rightTop + distance

sumValue = 0
for c in cvsList:
    diffA = abs(myLoc - c)
    diffB = fullLength - diffA
    sumValue += min(diffA, diffB)

print(sumValue)
