# Caroline Davis (cnd7cy)

import urllib.request

url = "http://cs1110.cs.virginia.edu/files/words.txt"
f = urllib.request.urlopen(url)
correctWords = []
correctWordsLower = []
for each in f:
    line = each.decode("utf-8").strip()
    correctWords.append(line)

for word in correctWords:
    wordLine = str(word)
    lowerWord = wordLine.lower()
    correctWordsLower.append(lowerWord)

print("Type text; enter a blank line to end. ")
while True:
    userTxt = input()
    if userTxt == "":
        break
    userWords = userTxt.strip(".?!,()\"\'").split()

    for word in userWords:
        cleanWord = word.strip(".?!,()\"\'")
        if cleanWord.lower() not in correctWordsLower:
            print("  MISSPELLED:", cleanWord)
