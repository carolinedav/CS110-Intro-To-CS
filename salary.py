# Caroline Davis (cnd7cy)
# Shirle Hinojosa (sh7wgz) helped me by telling me to split the function into multiple functions to aid in readability
# She also walked me through the methodology behind name_to_url
import urllib.request
import re

def name_to_url(name):
    """takes in the name and converts it to correct url format
    :param: name: string name used for finding the end of the url
    :return: name to be used in the url"""
    name = name.lower().replace(".", "")
    if "," in name:
        location = name.split(", ")
        name = location[1] + "-" + location[0]
    if " " in name:
        name = name.replace(" ", "-")
    return name

def jobTitle(name):
    """takes in the name and attaches to url base, finds job title
        :param: name: string name used for finding the end of the url
        :return: jobName: string value of the job title"""
    usedName = name_to_url(name)
    try:
        file = urllib.request.urlopen('http://cs1110.cs.virginia.edu/files/uva2018/' + usedName)
        for line in file:
            row = line.decode('utf-8').strip()
            job = re.compile(r'<span class="small text-muted" id="personjob">(.*)?</span>')

            match = re.search(job, row)
            if match:
                jobName = match.group(1)
                if "&amp" in jobName:
                    jobName = jobName.replace('&amp;', '&')
                if '&#39;' in jobName:
                    jobName = jobName.replace('&#39;', "'")
        return jobName
    except:
        return None


def salaryTitle(name):
    """takes in the name and attaches to url base, finds salary amount
            :param: name: string name used for finding the end of the url
            :return: salaryName: float value of the salary"""
    usedName = name_to_url(name)
    try:
        file = urllib.request.urlopen('http://cs1110.cs.virginia.edu/files/uva2018/' + usedName)
        for line in file:
            row = line.decode('utf-8').strip()
            salary = re.compile(r'<div style="margin:0; float:left; background:#337ab7; height:100%; width:<%= getPct\(paytype.amount, (.*)?\) %>%;"></div>')

            match = re.search(salary, row)
            if match:
                salaryName = match.group(1)
                if "$" in salaryName:
                    salaryName = salaeyName.replace('$', '')
        return float(salaryName)
    except:
        return 0

def rank(name):
    """takes in the name and attaches to url base, finds rank
            :param: name: string name used for finding the end of the url
            :return: rankName: int value of the salary ranking in the state of VA"""
    usedName = name_to_url(name)
    try:
        file = urllib.request.urlopen('http://cs1110.cs.virginia.edu/files/uva2018/' + usedName)
        for line in file:
            row = line.decode('utf-8').strip()
            rank = re.compile(r'<tr><td>University of Virginia rank</td><td>(.*)? of 8,582<!--not null --></td></tr>')

            match = re.search(rank, row)
            if match:
                rankName = match.group(1)
                rankName = rankName.replace(",", "")
        return int(rankName)
    except:
        return 0

def report(name):
    """takes in the name and compiles all three functions are above
            :param: name: string name used for finding the end of the url
            :return: the function calls of jobTitle, salaryTitle, and rank"""

    return jobTitle(name), salaryTitle(name), rank(name)
