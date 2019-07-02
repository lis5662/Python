# 4-1

pizza = ["Peperoni", "Four cheese", "Hawaiian", "Chicken with mushrooms"]
for favorite_pizza in pizza:
    print("This is my favorite pizza! " + favorite_pizza.upper() + " Yami- Yami" + "!")
print("I really love all of this pizzas!")


# 4-2

animals = ["dog", "cat", "monkey", "horse"]
for all_animals in animals:
    print("A " + all_animals.upper() + " would make a great pet\n" +
          "A " + all_animals.upper()  + " would make a great pet\n" +
          "The " + all_animals.upper()  + " will not be a good pet\n" +
          "A " + all_animals.upper()  + " would make a great pet")

print("Any of these animals would make a great pet!")


# 4-3

for i in range(1, 21):
    print(i)

# 4-4

#value = []
#for value in range(1, 1000000):
#    print(value)


# 4-5

#value = list(range(1, 1000000))
#print(min(value))
#print(max(value))
#print(sum(value))


# 4-6

odd_numbers = list(range(1, 21, 4))
print(odd_numbers)

# 4-7

three_numbers = []
for three_numbers in list(range(2, 31, 3)):
    print(three_numbers)

# 4-8

cube = []
for value in range(1, 10):
    cube.append(value**3)

#print(cube)


# 4-9

cube = [value ** 3 for value in range(1, 11)]
print(cube)


# 4-10

my_foods = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']

print("The first three items in the list are:")
print(my_foods[0:3])

print("Three items from the middle of the list are:")
print(my_foods[2:])

print("The last three items in the list are:")
print(my_foods[-3:])


# 4-11

pizza = ['Peperoni', 'Four cheese', 'Hawaiian', 'Chicken with mushrooms']
friends_pizzas = pizza[:]           # копирование списка с помощью среза [:]

pizza.append('Margarita')
friends_pizzas.append('Chili')

print("My favorite pizzas are:")    # выводим первый список с помощью цикла for
for my_fav_pizza in pizza:
    print(pizza)


print("\nMy favorite pizzas are:")    # выводим второй список с помощью цикла for
for my_fav_pizza in friends_pizzas:
    print(friends_pizzas)


# 4-12

my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]

my_foods.append('cannoli')
friends_foods.append('ice cream')

print("My favorite foods are:")
for fav_foods in my_foods:
    print(my_foods)


print("\nMy friend's favorite foods are:")
for fav_foods in friends_foods:
    print(friends_foods)

# 4-13

sweden_smorgasbord = ('hummus', 'pizza', 'fried fish', 'salad', 'chicken')
print("Today in our menu:")
for food in sweden_smorgasbord:
    print(food)

print("The restaurant is changing two new dishes:")

sweden_smorgasbord = ('eggs with bacon', 'pizza', 'fried fish', 'salad', 'hamburger')
print("New menu:")
for new_menu in sweden_smorgasbord:
    print(new_menu)



# 4-14
"""Посмотреть исходное руководство 
PEP 8"""


# 4-15

