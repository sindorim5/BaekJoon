def solution(X, Y):
    arr = []

    for element in list(set(X) & set(Y)):
        countX = X.count(element)
        countY = Y.count(element)

        for _ in range(min(countX, countY)):
            arr.append(element)

    if not arr:
        return "-1"
    elif max(arr) == "0":
        return "0"
    else:
        arr = sorted(arr, reverse=True)
        return "".join(arr)
