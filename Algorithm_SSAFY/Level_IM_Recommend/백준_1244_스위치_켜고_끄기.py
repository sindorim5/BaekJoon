import sys

sys.stdin = open("./input.txt", "r", encoding="utf-8")

n = int(input())
switchList = list(map(int, input().split()))

# 위치 맞추기
switchList.insert(0, -1)

student = int(input())
setList = []
for _ in range(student):
    setList.append(list(map(int, input().split())))


def changeSwitch(index):
    if switchList[index] == 0:
        switchList[index] = 1
    else:
        switchList[index] = 0


for s in setList:
    gender, number = s[0], s[1]

    if gender == 1:
        for i in range(number, len(switchList), number):
            changeSwitch(i)
    else:
        changeSwitch(number)
        for i in range(n // 2):
            if (number + i) > n or (number - i) < 1:
                break
            if switchList[number + i] == switchList[number - i]:
                changeSwitch(number + i)
                changeSwitch(number - i)
            else:
                break

for i in range(1, len(switchList)):
    print(switchList[i], end=" ")
    if i % 20 == 0:
        print()
