#open file
rawText = open('romeo.txt')

#find unique words in text file line by line and add them to uniqueWords
uniqueWords = []
for line in rawText:
    line = line.rstrip()
    lineList = line.split()

    i = 0
    for word in lineList:
        if not lineList[i] in uniqueWords:
            uniqueWords.append(word)
        i = i + 1

#sort the unique words alphebetically and print them
uniqueWords.sort()
print(uniqueWords)
