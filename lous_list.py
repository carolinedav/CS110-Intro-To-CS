# Caroline Davis (cnd7cy)

import urllib.request

def instructors(department):
    """returns an alphabetically-sorted list containing every instructor in lou's list for the inputted department.
        each instructor will only be listed once
        :param: department: string value of the department in question to be appended to the url
        :return: alphabetical list of all instructors in a given department (str values)"""
    url = "http://cs1110.cs.virginia.edu/files/louslist/" + department
    f = urllib.request.urlopen(url)
    finalList = []
    for each in f:
        line = each.decode("utf-8").strip().split("|")
        instructor = line[4]
        location = instructor.find("+")
        instructorName = instructor[0:location]
        if instructorName not in finalList:
            finalList.append(instructorName)
            finalList.sort()
    f.close()
    print(finalList)

def class_search(dept_name, has_seats_available = True, level = None, not_before = None, not_after = None):
    """returns a list of lists that holds all needed information for all the classes that meet the required criteria
            :param: dept_name: given department value (str) that is appended to the url
            :param: has_seats_available: checks that current enrollment is not > or = to the allowable enrollment; if
                                         set to false, then the open seat space does not matter (boolean value)
            :param: level: 4-digit int value that must match the level of the classes; if None, level does not matter
            :param: not_before: int value that excludes all classes that start before the time given; if None, the
                                the start time will not be limited
            :param: not_after: int value that excludes all classes that start ater the time given; if None, the
                                the start time will not be limited
            :return: alphabetical list of all instructors in a given department (str values)"""
    louList = []
    url = "http://cs1110.cs.virginia.edu/files/louslist/" + dept_name
    f = urllib.request.urlopen(url)
    for each in f:
        line = each.decode("utf-8").strip().split("|")
        department = line[0]
        course_number = line[1]
        section = line[2]
        course_title = line[3]
        instructor = line[4]
        typeClass = line[5]
        hours = line[6]
        monday = line[7]
        tuesday = line[8]
        wednesday = line[9]
        thursday = line[10]
        friday = line[11]
        startTime = line[12]
        endTime = line[13]
        location = line[14]
        enrollment = line[15]
        allowableEnrollment = line[16]
        checking = 0

        if has_seats_available:
            if int(enrollment) < int(allowableEnrollment):
                checking += 1
        else:
            checking += 1

        if level is not None:
            strLevel = str(level)
            if int(course_number[0]) == int(strLevel[0]):
                checking += 1
        else:
            checking += 1

        if not_before is not None:
            if int(startTime) >= not_before:
                checking += 1

        if not_after is not None:
            if int(startTime) <= not_after:
                checking += 1
                if checking == 4:
                    louList.append(line)
        else:
            checking += 1
            if checking == 4:
                louList.append(line)

    f.close()
    return(louList)
