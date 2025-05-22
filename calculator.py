import sys

def calculator(num1, num2, operator):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print('Cannot divide by zero')
            return
        else:
            result = num1 / num2
    else:
        print('Invalid operator')
        return

    if result == int(result):
        print(int(result))
    else:
        print(result)

while True:
    try:
        num1 = float(input('Enter first number: '))
        operator = input('Enter operator: ')
        num2 = float(input('Enter second number: '))
        calculator(num1, num2, operator)
    except ValueError:
        print('Please enter a number.')
    again = input('Do you want to continue? (y/n): ')
    if again.lower() == 'n':
        break

