import sys, os

print('The command line arguments are:')
for i in sys.argv:
    print(i)

print('\n\nThe PYTHONPATH is', sys.path, '\n')

print(os.getcwd())


from math import sqrt
print("Square root of 16 is", sqrt(16))