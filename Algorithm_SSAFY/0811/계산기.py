inputLine = "3+(4/2-(5*3+2/2-1)+10+(3*4)/2)"
stack = []
result = []
for i in inputLine:
    if "0" <= i <= "9":
        result.append(i)
    else:
        if i == "(":
            stack.append(i)
        elif i == "*" or i == "/":
            while stack and (stack[-1] == "*" or stack[-1] == "/"):
                result.append(stack.pop())
            stack.append(i)
        elif i == "+" or i == "-":
            while stack and stack[-1] != "(":
                result.append(stack.pop())
            stack.append(i)
        elif i == ")":
            while stack and stack[-1] != "(":
                result.append(stack.pop())
            stack.pop()

while stack:
    result.append(stack.pop())

print("".join(result))
