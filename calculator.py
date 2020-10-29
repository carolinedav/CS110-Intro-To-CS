# Caroline Davis (cnd7cy)

def binop(mathEx):

    '''
    binop is a function that evaluates simple mathematical expressions
    :param mathEx: mathEx = math expression (String) representing simple mathematical expressions
    :return: returns either an int or float value of the expression
    '''
    
    if "+" in mathEx:
        operator = mathEx.find("+")
        firstNum = int(mathEx[0: operator])
        secondNum = int(mathEx[operator + 1: len(mathEx)])
        return firstNum + secondNum

    elif "-" in mathEx:
        operator = mathEx.find("-")
        firstNum = int(mathEx[0: operator])
        secondNum = int(mathEx[operator + 1: len(mathEx)])
        return firstNum - secondNum

    elif "/" in mathEx:
        operator = mathEx.find("/")
        firstNum = int(mathEx[0: operator])
        secondNum = int(mathEx[operator + 1: len(mathEx)])
        return firstNum / secondNum

    elif "*" in mathEx:
        operator = mathEx.find("*")
        firstNum = int(mathEx[0: operator])
        secondNum = int(mathEx[operator + 1: len(mathEx)])
        return firstNum * secondNum
