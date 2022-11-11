def computeGrade (score) :
    if score > 1.0 : grade = 'Number out of range'
    elif score < 0 : grade = 'Number out of range'
    elif score >= 0.9 : grade = 'A'
    elif score >= 0.8 : grade = 'B'
    elif score >= 0.7 : grade = 'C'
    elif score >= 0.6 : grade = 'D'
    else : grade = 'F'
    return grade


score = input('Enter a score between 0.0 and 1.0: ')
try:
    ival = float(score)
except:
    print('Error, please enter a numeric input')
    quit()

score = float(score)
print(computeGrade(score))
