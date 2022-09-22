# [1,2,3,4,5,6,7,8,9,10] 의 부분집합 중 합이 10인 부분집합을 구하라

visited = [False for _ in range(11)]

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 10


def comb(arr, n):
    result = []
    if n > len(arr):
        return result

    if n == 1:
        for i in arr:
            result.append([i])
    elif n > 1:
        for i in range(len(arr) - n + 1):
            for j in comb(arr[i+1:], n-1):
                result.append([arr[i]] + j)

    return result


def combination(arr, r):
    # 1.
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]

    # 2.
    def generate(chosen):
        if len(chosen) == r:
            print(chosen)
            return

        # 3.
        if chosen:
            start = arr.index(chosen[-1]) + 1
        else:
            start = 0
        for nxt in range(start, len(arr)):
            if used[nxt] == 0 and (nxt == 0 or arr[nxt-1] != arr[nxt] or used[nxt-1]):
                chosen.append(arr[nxt])
                used[nxt] = 1
                generate(chosen)
                chosen.pop()
                used[nxt] = 0
    generate([])
