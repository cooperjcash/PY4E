hours = input('Enter Hours: ')
rate = input('Enter Rate: ')
hours = float(hours)
rate = float(rate)

if hours <= 40:
    pay = hours * rate
    print('Pay:',pay)
else:
    xhours = hours - 40
    pay = (rate * 40) + (xhours * (rate * 1.5))
    print('Pay:',pay)
