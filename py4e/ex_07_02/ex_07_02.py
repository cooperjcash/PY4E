#enter file name and catch bad file names
fileName = input('Enter file name: ')
try:
    fileRaw = open(fileName)
except:
    #check if it is easter
    if fileName == 'na na boo boo':
        print("NA NA BOO BOO TO YOU - You have been punk'd, get rekt kid!")
    #it is not easter
    else:
        print('invalid file name')
    quit()

#go line by line and check for spam confidence lines
total = 0
count = 0
for line in fileRaw:
    #if spam confidence line extract the spam confidence value
    if line.startswith('X-DSPAM-Confidence: '):
        #counts total number of spam confidence lines
        count = count + 1
        #finds colon on line and extracts float value
        colonLoc = line.find(':')
        extractedNum = line[colonLoc+1:].strip()
        extractedNum = float(extractedNum)
        #running total of values
        total = total + extractedNum

#calculate and print average
avg = total / count
print('Average spam confidence:',avg)
