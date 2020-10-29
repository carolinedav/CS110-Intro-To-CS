# Caroline Davis (cnd7cy)

cGPA = 0
cCredit = 0

def add_course(gpa1, credit = 3):  # Maia Jenckes (mcj9ax) helped with the one argument problem
    global cGPA
    global cCredit
    cCredit += credit
    cGPA = float(((cGPA * (cCredit - credit)) + (gpa1 * credit)) / cCredit)

def gpa():
    return cGPA

def credit_total():
    return cCredit
