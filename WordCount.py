# created by harsha matta
# created  on 1/10/18
#  this program takes a file. Then it outputs how many of each word there is.

# Read file
from typing import List


inputFile = open("mywords.txt","r")

# Declare a dictionary
wordDict = {}

# Get each line
for line in inputFile:
    # split the words
    wordList = line.split()
    #
    for word in wordList:
        cnt = wordDict.get(word)
        if cnt == None:
            wordDict[word] = 1
        else:
            cnt = cnt + 1
            wordDict[word] = cnt


# Print dictionary


import operator
sorted_d: List[str] = sorted(wordDict.items(), key=operator.itemgetter(1))


for x in sorted_d:
    print(x)
...