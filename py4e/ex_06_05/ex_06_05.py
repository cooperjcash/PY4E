str = 'X-DSPAM-Confidence: 0.8475 '

#search the above string and extract only the decimal number and store it
colonLoc = str.find(':')
extractedNum = str[colonLoc+1:].strip()
extractedNum = float(extractedNum)
print(extractedNum)
