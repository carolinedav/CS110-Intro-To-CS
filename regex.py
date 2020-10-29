# Caroline Davis (cnd7cy)
import re

pattern = r"[\S]+"  # found \S from the textbook
nospace = re.compile(pattern, re.IGNORECASE)  # ignorecase from https://docs.python.org/3/library/re.html

secondPattern = r'"\S(.*?)\S"'
quotation = re.compile(secondPattern, re.IGNORECASE)

thirdPattern = r'(-?[0-9]+(\.[0-9]+)?)(,|, | )(-?[0-9]+(\.[0-9]+)?)'  # https://www.tutorialspoint.com/python/python_
# reg_expressions.htm helped!

twonum = re.compile(thirdPattern, re.IGNORECASE)