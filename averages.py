# Caroline Davis (cnd7cy)

def mean(a, b, c):
    return (a + b + c) / 3

def median(a, b, c):
    if b <= a <= c or c <= a <= b:
        median1 = a
    elif a <= b <= c or c <= b <= a:
        median1 = b
    else:
        median1 = c
    return median1

def rms(a, b, c):
    return mean(a**2, b**2, c**2) ** (1/2)


def middle_average(a, b, c):
    mFinal = mean(a, b, c)
    medFinal = median(a, b, c)
    rFinal = rms(a, b, c)
    midAveFinal = median(mFinal, medFinal, rFinal)
    return midAveFinal
