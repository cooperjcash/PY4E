#Hours worked input and exception handling
hours = input('Enter Hours: ')
try:
    ival = float(hours)
except:
    print('Error, please enter a numeric input')
    quit()
#Hourly rate input and exception handling
rate = input('Enter Rate: ')
try:
    ival = float(rate)
except:
    print('Error, please enter a numeric input')
    quit()
#Change hours and rate into float type
hours = float(hours)
rate = float(rate)
#Calculate pay if normal hours worked
if hours <= 40:
    pay = hours * rate
    print('Pay:',pay)
#Calculate pay if overtime hours worked
else:
    xhours = hours - 40
    pay = (rate * 40) + (xhours * (rate * 1.5))
    print('Pay:',pay)
