myName = input("What is your name? ")  # ask for their name
birthMonth = input('What month were you born in? ')

print('Hello ' + myName)
if birthMonth == 'January':
    print('Happy birthday month! ')
else:
    print('Not birthday month :(')
print('There are ', len(myName), ' letters in your name')
