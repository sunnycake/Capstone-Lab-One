classCount = int(input('How many classes are you taking this semester? '))
total = []
for classType in range(classCount):
    className = input('Enter the name of the class: ')
    total.append(className)

print('The classes you are taking are: ' + str(total))
