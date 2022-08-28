import sys

sys.stdin = open("algorithm_study/SW역량테스트/shuffle.txt", "r", encoding="UTF-8")

T = int(input())


def my_shuffle(l, r, i):
    global N
    new_lst = []
    l_idx, r_idx = 0, 0

    while l_idx < N//2:
        new_lst.append(l[l_idx])
        if l_idx >= i:
            new_lst.append(r[r_idx])
            r_idx += 1
        l_idx += 1

    while r_idx < N//2:
        new_lst.append(r[r_idx])
        r_idx += 1

    new_l, new_r = new_lst[0:N//2], new_lst[N//2:]
    return new_l, new_r


def dfs(left, right, cnt):
    global result, N
    if cnt >= result:
        return
    if left+right == sol1 or left+right == sol2:
        result = min(cnt, result)
        return
    for i in range(N//2):
        new_left, new_right = my_shuffle(left, right, i)
        dfs(new_left, new_right, cnt+1)
        new_left, new_right = my_shuffle(right, left, i)
        dfs(new_left, new_right, cnt+1)
    return


for test_case in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    card1, card2 = lst[0:N//2], lst[N//2:]

    sol1 = sorted(lst)
    sol2 = sorted(lst, reverse=True)

    result = 6
    dfs(card1, card2, 0)
    if result >= 6:
        print("#{} {}".format(test_case, -1))
    else:
        print("#{} {}".format(test_case, result))
