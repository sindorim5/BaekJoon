import sys

sys.stdin = open("input.txt", "r", encoding="utf-8")

N, K = map(int, input().split())
result = 0
# 여학생 0, 남학생 1
boys = [0, 0, 0, 0, 0, 0]
girls = [0, 0, 0, 0, 0, 0]

for i in range(N):
    gender, grade = map(int, input().split())
    if gender == 0:
        girls[grade - 1] += 1
    else:
        boys[grade - 1] += 1

for i in boys:
    result += i // K
    if i % K > 0:
        result += 1

for i in girls:
    result += i // K
    if i % K > 0:
        result += 1

print(result)
