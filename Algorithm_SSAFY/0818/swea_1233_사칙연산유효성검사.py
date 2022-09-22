import sys

sys.stdin = open("1233_input.txt", "r", encoding="utf-8")

input = sys.stdin.readline


def checkOP(nodeData):
    if nodeData in ["+", "-", "*", "/"]:
        return True
    return False


T = 10

for test_case in range(1, T + 1):
    n = int(input())
    half = n // 2
    result = 1
    for i in range(n):
        node = input().split()
        nodeNum = int(node[0])
        nodeData = node[1]
        if nodeNum <= half:
            if not checkOP(nodeData):
                result = 0
        else:
            if checkOP(nodeData):
                result = 0
    print("#{} {}".format(test_case, result))


"""
완전 이진트리이므로 리프노드들은 숫자, 나머지 노드들은 연산자여야 연산이 가능하다
전체 노드의 수를 n이라 했을 때 n//2+1노드까지는 자식 노드가 있고 그 후부터 모두 리프노드가 된다
따라서 n//2+1번 노드까지 모두 연산자인지 확인, 나머지 노드들은 숫자인지 확인해주면 된다
"""
