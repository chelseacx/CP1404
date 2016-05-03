import string

text = input("Text: ")

wordList = text.strip(string.punctuation).split()

wordDict = {}

for word in wordList:
    if word not in wordDict:
        wordDict[word] = 1
    else:
        wordDict[word] += 1

sort_keys = sorted(wordDict.keys())

for key in sort_keys:
    print("{} : {}".format(key, wordDict[key]))

