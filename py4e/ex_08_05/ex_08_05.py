#enter file name and catch bad file names
fileName = input('Enter file name: ')
try:
    fileRaw = open(fileName)
except:
    print('invalid file name')
    quit()

numEmails = 0
#search the file for emails
for line in fileRaw:
    if line.startswith('From '):
        #increment number of emails
        numEmails = numEmails + 1
        #print out the sender
        line = line.split()
        print(line[1])

#print the total number of emails
print('There were',numEmails,'lines in the file with From as the first word')
