import sys

sys.stdin = open("input.txt", "r", encoding="utf-8")
input = sys.stdin.readline


N, K = map(int, input().split())
tempList = list(map(int, input().split()))

result = []
result.append(sum(tempList[:K]))

for i in range(N - K):
    result.append(result[i] - tempList[i] + tempList[K + i])

print(max(result))
