# Caroline Davis (cnd7cy)

def check(creditCard):
    """ this function accepts a single positive integer input and returns
    True if the input is a valid credit card number
    :param: creditCard = positive integer input
    :return: True if the input is a valid credit card number OR
    :return: False if the input is not a valid credit card number"""
    strCreditCard = str(creditCard)
    sum1 = 0
    sum2 = 0
    step = 0
    for each in range(len(strCreditCard) // 2):
        if len(strCreditCard) % 2 == 0:
            sum1 += int(strCreditCard[1 + step])
            num2 = str(2 * int(strCreditCard[0 + step]))
            countNum2 = 0
            for num in range(len(num2)):
                sum2 += int(num2[countNum2])
                countNum2 += 1
        else:
            sum1 += int(strCreditCard[0 + step])
            num2 = str(2 * int(strCreditCard[1 + step]))
            countNum2 = 0
            for num in range(len(num2)):
                sum2 += int(num2[countNum2])
                countNum2 += 1
        step += 2

    final = sum1 + sum2  # adds the two sums calculated

    if final % 10 == 0 and final != 0:  # if the result is a multiple of 10, it is a valid number
        return True
    else:
        return False
