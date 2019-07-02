# def divide(a, b):
    # try:
    #     return a/b
    # except ZeroDivisionError:
    #     print("Don't divide by zero please!")
    # except TypeError as err:
    #     print("a and b must be ints or floats")
    #     print(err)
    # else:
    #     print(f"{a} divided by {b} is {result}")



def divide(a, b):
     try:
         return a/b
     except (ZeroDivisionError, TypeError) as err:
         print("Something went wrong!")
         print(err)
     else:
         print(f"{a} divided by {b} is {result}")

print(divide(1,2))
print(divide(1,0))