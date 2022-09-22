def solution():
    q = [0 for _ in range(100)]
    front, rear, candy = -1, -1, 20

    def printQ():
        print("front+1: {}, rear+1: {}".format(front+1, rear+1))
        print("[", end="")
        for i in range(front + 1, rear + 1):
            print(q[i], end=" ")
        print("]\n", end="")

    studentNum = 1
    incommingNum = 2

    studentCan = [1 for i in range(20)]

    rear += 1
    q[rear] = studentNum
    print("==>{}번 학생 : 입장하여 줄을 선다.".format(studentNum))
    printQ()

    front += 1
    studentNum = q[front]
    print("{}번 학생 : 줄에서 나와...".format(studentNum))
    printQ()

    while candy > 0:
        candy -= studentCan[studentNum]
        print("{}번 학생 : 선생님한테 사탕 {}개를 받는다.".format(
            studentNum, studentCan[studentNum]))
        print("===== 남은 사탕의 개수는 {}개다.\n".format(candy))
        studentCan[studentNum] += 1

        if candy <= 0:
            print(studentNum)
            break

        rear += 1
        q[rear] = studentNum
        print("{}번 학생 : 다시 줄을 선다.".format(studentNum))
        printQ()
        print("==>{}번 학생 : 입장하여 줄을 선다.".format(incommingNum))
        rear += 1
        incommingNum += 1
        q[rear] = incommingNum
        printQ()
        front += 1
        studentNum = q[front]
        print("{}번 학생 : 줄에서 나와...".format(studentNum))
        printQ()


solution()
