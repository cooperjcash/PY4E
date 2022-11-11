#Define all variables
total = 0
avg = None
i = 0
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
    total = total + userInput
    i = i + 1
#div by zero handling
try :
    avg = total / i
except :
    avg = 0
#print sum, total number of integers, and average
print('Sum:',int(total),'Total ints:',i,'Average:',avg)
