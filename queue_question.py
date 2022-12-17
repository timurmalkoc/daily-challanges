def evalRPN(tokens):
    nums = []
    for token in tokens:
        if token not in '+-*/':
            nums.append(int(token))
        else:
            right_num, left_num = nums.pop(), nums.pop()
            if token == '+':
                nums.append(left_num + right_num)
            elif token == '-':
                nums.append(left_num - right_num)
            elif token == '/':
                nums.append(int(float(left_num) / right_num))
            else:
                nums.append(left_num * right_num)
    return nums.pop()


print(evalRPN(["2","1","+","3","*"]))
print(evalRPN(["4","13","5","/","+"]))
print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))