
"""Problem no. 1"""
numbers = []
for i in range(5):
    number = int(input('Number: '.format(numbers)))
    numbers.append(number)
# while len(numbers) < 5:
#     numbers.append(number)
#     number = int(input('Number: '.format(numbers)))
print('The first number is {}'. format(numbers[0]))
print('The last number is {}'.format(numbers[-1]))  # figure this out
print('The smallest number is', min(numbers))
print('The largest number is', max(numbers))
print('The average of the numbers is', sum(numbers) / len(numbers))


"""Problem no. 2"""
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
             'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
             'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input('Username: ')
if username in usernames:
    print("Access granted")
else:
    print("Access denied")
    username = input('Username: ')

