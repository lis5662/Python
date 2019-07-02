x = int(input('Enter first value: '))
y = int(input('Enter second value: '))
operation = input('Operation: ')

result = None

if operation == '+':
    result = x + y
elif operation == '-':
    result = x - y
elif operation == '*':
    result = x * y
elif operation == '/':
    result = x / y
elif operation == '%':
    result = x % y

else:
    print('Unsupported operation!')

if result is not None:
    print('Result: ', result)
