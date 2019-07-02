# Example 1 base
def square_of_7():
    print("I AM BEFORE THE RETURN!")
    return 7**2
    print("I AM AFTER THE RETURN!")

result =square_of_7()
print(result)

# Example 1 with function parameter
def square(num):
    return num * num

print(square(4))
print(square(8))

# Example 2 base
def sign_happy_birthday():
    print("Happy Birthday To You!")
    print("Happy Birthday To You!")
    print("Happy Birthday To You!")
    print("Happy Birthday To You!")

sign_happy_birthday()
sign_happy_birthday()

# Example 2 with function parameter
def sing_happy_birthday(name):
    print("Happy Birthday To You!")
    print("Happy Birthday To You!")
    print(f"Happy Birthday dear {name}")
    print("Happy Birthday To You!")

sing_happy_birthday("Rashida")
sing_happy_birthday("Nicholas")

