def display_names(first, second):
    print(f"{first} says hello to {second}")

names = {"first": "Colt", "second": "Rusty"}

# display_names(first="Charlie", second="Sue")
# display_names(names) # nope...
display_names(**names) # nope...
# display_names(first="Colt", second="Rusty")



def add_and_multiply_numbers(a,b,c,**kwargs):
    print(a + b * c)
    print("OTHER STUFF....")
    print(kwargs)

data = dict(a=1,b=2,c=3,d=55,name="Tony")

# add_and_multiply_numbers(data) # TypeError
add_and_multiply_numbers(**data, cat="blue") # 7