age = 20
name = 'Dima'

print('{0} was {1} years old when he wrote this book'.format(name, age))
print('Why is {0} playing with that python?'.format(name))

# From Python 3.6 we can use f-string method. This is the short method for format strings!

age = 20
name = 'Dima'

print(f'{name} was {age} years old when he wrote this book')
print(f'Why is {name} playing with that python?')


# decimal (.) precision of 3 for float '0.333'
print('{0:.3f}'.format(1.0/3))

# fill with underscores (_) with the text centered
# (^) to 11 width '__hello__'
print('{0:_^11}'.format('hello'))

# keyword-based 'Swarrop wrote A Byte of Python'
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))

# Escape Sequences \n
print('This is the first line\nThis is the second line.')

# \t
print("This is the first sentence. \
This is the second sentence.")