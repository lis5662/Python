# global scope
total = 0

def increment():
    global total
    total += 1
    return total
print(increment()) # Error!

name = "Rusty"

# nonlocal

def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner()