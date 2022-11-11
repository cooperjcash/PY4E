fileName = input('Enter file name: ')

fileRaw = open(fileName)
for line in fileRaw :
    line = line.upper().rstrip()
    print(line)
