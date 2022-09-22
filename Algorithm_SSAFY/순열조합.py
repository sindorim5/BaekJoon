def permutation(target, arr):
    result = []
    visited = [False for _ in range(len(arr))]

    def nowPermute(nowArr):
        if len(nowArr) == target:
            result.append(nowArr)
            return
        for i in range(len(arr)):
            if not visited[i]:
                visited[i] = True
                nowPermute(nowArr + [arr[i]])
                visited[i] = False

    nowPermute([])
    return result


def combination(target, arr):
    result = []

    def nowCombi(idx, nowArr):
        if len(nowArr) == target:
            result.append(nowArr)
            return
        for i in range(idx, len(arr)):
            nowCombi(i+1, nowArr + [arr[i]])

    nowCombi(0, [])
    return result


def subset(arr):
    result = []

    for i in range(len(arr)):
        com = combination(i, arr)
        result.append(com)
    return result


arr = [1, 2, 3]

per = permutation(2, arr)

com = combination(2, arr)

sub = subset(arr)

print("**********순열**********")
print(per)
print("**********조합**********")
print(com)
print("**********부분**********")
print(sub)
