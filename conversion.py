# Caroline Davis (cnd7cy)

def c2f(celsiusTemp):
    cFahrenTemp = round(((celsiusTemp * (9 / 5)) + 32), 1)
    return cFahrenTemp

def f2c(fahrenheitTemp):
    cCelsiusTemp = (fahrenheitTemp - 32) * (5/9)
    return cCelsiusTemp
