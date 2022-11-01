n = int(input())

aList = list(map(int, input().split()))
bList = list(map(int, input().split()))


def calculate():
    result = 0
    for i in range(n):
        result += aList[i] * bList[i]

    return result

aList.sort()
bList.sort(reverse=True)

print(calculate())