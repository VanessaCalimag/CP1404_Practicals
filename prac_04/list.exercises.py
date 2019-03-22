
def main():
    numbers = []
    number = int(input('Number: '.format(numbers)))
    while len(numbers) < 5:
        numbers.append(number)
        number = int(input('Number: '.format(numbers)))
    print('The first number is {}'. format(numbers[0]))
    print('The last number is {}'.format(numbers[-1]))  # figure this out
    print('The smallest number is', min(numbers))
    print('The largest number is', max(numbers))
    print('The average of the numbers is', sum(numbers) / len(numbers))


main()
