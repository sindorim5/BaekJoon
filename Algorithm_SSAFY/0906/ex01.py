# input
# 0000000111 1000000110 0000011110 0110000110 0001111001 1110011111 1001100111

input = "0000000111100000011000000111100110000110000111100111100111111001100111"
inputList = list(input)
result = []
i = 0
while i <= len(inputList) - 7:
    temp = inputList[i:i+7]
    print("".join(temp))
    number = int("".join(temp), 2)
    result.append(number)
    i += 7

print(result)
