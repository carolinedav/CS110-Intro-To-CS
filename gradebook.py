# Caroline Davis (cnd7cy)
# Maia Jenckes (mcj9ax) helped me to understand the logic behind the assignment

dictGrades = {}

def assignment(kind, grade, weight = 1):

    """ Creates a dictionary containing the grades for each type of assignment and the corresponding
    weight of each grade.
    :param: kind: the type of assignment to be used as the dictionary key; string
    :param: grade: grade of the assignment, 0 - 100; int/float
    :param: weight: the weight of an individual assignment, if not specified it is assumed to be 1; int/float
    :return: dictGrades: a dictionary containing the grades"""

    global dictGrades

    if kind in dictGrades:
        dictGrades[kind] += [[grade, weight]]
    else:
        dictGrades[kind] = [[grade, weight]]
    return dictGrades


def total(proportions):

    """For every assignment type, computes all the grades multiplied by their weight, divides the sum by
    the total worth of all assignments, then multiples the result by the weight of the assignment type
    :param: proportions: dictionary of assignment grades and their corresponding weights
    :return: finalGrade: cumulative total grade based on the proportions dictionary"""

    finalGrade = 0

    for key in proportions:
        totalGrade = 0
        totalWeight = 0

        if key in dictGrades:
            if key in dictGrades:
                for each in dictGrades[key]:
                    totalGrade += each[0] * each[1]
                    totalWeight += each[1]
                averageGrade = totalGrade / totalWeight
                finalGrade += proportions[key] * averageGrade
            else:
                finalGrade += 0

    return finalGrade
