
#create list to store only numbers input
numList = []
numInput = 'empty'

#execute infinitely until any case of 'done' is input
while numInput.lower() != 'done':
    numInput = input('Enter a number: ')
    try:
        #make sure an input is a number
        float(numInput)
    except:
        if numInput.lower() == 'done':
            continue
        print('invalid input')

    #add input number to the list of numbers
    numList.append(float(numInput))

#print out max and min of the list if list isn't empty
if len(numList) != 0:
    print('Maximum:',max(numList))
    print('Minimum:',min(numList))
else:
    print('No numbers were input')
