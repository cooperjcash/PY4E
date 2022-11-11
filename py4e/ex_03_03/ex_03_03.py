score = input('Enter a score between 0.0 and 1.0: ')
try:
    ival = float(score)
except:
    print('Error, please enter a numeric input')
    quit()

score = float(score)

if score > 1.0 : print('Number out of range')
elif score < 0 : print('Number out of range')
elif score >= 0.9 : print('A')
elif score >= 0.8 : print('B')
elif score >= 0.7 : print('C')
elif score >= 0.6 : print('D')
else : print('F')
