#Define all variables
i = 0
maxInt = None
minInt = None
userInput = 'notDone'
#Ask user for input until done is entered
while userInput != 'done' :
    userInput = input('Enter an integer: ')
    if userInput == 'done' or userInput == 'Done' :
        break
    try :
        userInput = float(userInput)
    except :
        print('Invalid input')
        continue
    if i == 0 :
        maxInt = userInput
        minInt = userInput
    else :
        if userInput > maxInt :
            maxInt = userInput
        elif userInput < minInt :
            minInt = userInput
    i = i + 1
#print max int, and min int
print('Maximum is',int(maxInt))
print('Minimum is',int(minInt))
