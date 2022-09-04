import sys
from collections import deque
sys.stdin = open("algorithm_study/SW역량테스트/shuffle.txt", "r", encoding="UTF-8")

T = int(input())


def shuffle(x, cards):
    result = []

    if x < N//2:
        L = deque(cards[:N//2])
        R = deque(cards[N//2:])
        num = N//2 - x
    else:
        L = deque(cards[N//2:])
        R = deque(cards[:N//2])
        num = x - (N//2) + 1

    for _ in range(num):
        result.append(L.popleft())

    while len(R) > num:
        result.append(R.popleft())
        result.append(L.popleft())

    while R:
        result.append(R.popleft())

    return result


def mixed(cnt, cards):
    global answer

    if cnt >= answer or cnt > 5:
        return

    if cards == sort_cards or cards == r_sort_cards:
        answer = min(answer, cnt)
        return

    for i in range(1, N):
        mixed(cnt+1, shuffle(i, cards))


for test_case in range(1, T+1):
    N = int(input())
    cards = list(map(int, input().split()))

    sort_cards = sorted(cards)
    r_sort_cards = sorted(cards, reverse=True)

    answer = float('inf')

    mixed(0, cards)

    if answer > 5:
        answer = -1

    print("#{} {}".format(test_case, answer))
