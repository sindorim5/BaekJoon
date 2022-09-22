n = int(input())

answer = 0
row = [0] * n


def promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    return True


def nQueen(x):
    global answer
    if x == n:
        answer += 1
        return
    else:
        for i in range(n):
            row[x] = i
            if promising(x):
                nQueen(x + 1)


nQueen(0)

print(answer)
