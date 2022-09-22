# [1,2,3,4,5,6,7,8,9,10] 의 부분집합 중 합이 10인 부분집합을 구하라

visited = [False for _ in range(11)]

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 10

check = [0] * (n + 1)
result = []


def dfs(v):
    if v == n + 1:
        temp = []
        for i in range(1, n+1):
            if check[i] == 1:
                temp.append(i)
        if sum(temp) == 10:
            result.append(temp)
    else:
        check[v] = 1
        dfs(v+1)
        check[v] = 0
        dfs(v+1)


dfs(1)

print(result)
