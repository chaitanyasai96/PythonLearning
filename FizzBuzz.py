choice = ''

while choice.lower() != 'quit':
    number = int(input('Enter the number: '))
    if choice.lower() != quit:
        def fizzbuzz(number):
            if number % 3 == 0 and number % 5 == 0:
                return 'Fizz-Buzz'
            elif number % 5 == 0:
                return 'Buzz'
            elif number % 3 == 0:
                return 'Fizz'
            else:
                return 'Neither Fizz nor Buzz'
    print(fizzbuzz(number))
    choice = input("Enter any key to continue or quit to exit")
else:
    print("See you Soon")


