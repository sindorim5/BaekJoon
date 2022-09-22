# input
# 01D06079861D79F99F

input = "01D06079861D79F99F"
inputList = list(input)
result = []
i = 0

decimalValue = int(input, 16)
binaryValue = bin(decimalValue)
binaryValue = binaryValue[2:]

while i <= len(binaryValue) - 7:
    temp = binaryValue[i:i+7]
    print(temp)
    number = int("".join(temp), 2)
    result.append(number)
    i += 7

print(result)
