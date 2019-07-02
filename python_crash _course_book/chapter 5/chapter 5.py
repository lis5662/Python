cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


# Проверка условий, равенства
car = 'bmw'
if car == 'bmw':
    print(True)
else:
    print(False)


# Проверка равенств без учета регистра

# car = 'Audi'
# car == 'audi'

# car = 'Audi'
# car.lower() == 'audi'

# Проверка неравенства

requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

# Сравнения чисел

# age = 18
# age == 18
# True


answer = 16
if answer != 42:
    print("That is not the correct answer. Please try again!")


age = 19
if age <= 21:
    print(True)
elif age > 21:
    print(False)


# Проверка нескольких условий and и or

# Использование and для проверки условий
age_0 = 22
age_1 = 18
if age_0 >= 21 and age_1 >= 21:
    print(True)
else:
    print(False)


age_1 = 22
if age_0 >= 21 and age_1 >= 21:
    print(True)
else:
    print(False)

# использование or для проверки условий

age_0 = 22
age_1 = 18
if age_0 >= 21 or age_1 >= 21:
    print(True)
else:
    print(False)


age_0 = 18
if age_0 >= 21 or age_1 >= 21:
    print(True)
else:
    print(False)

# Проверка вхождения в список in

requested_topping = ['mushrooms', 'onions', 'pineapple']
if 'mushrooms' in requested_topping:
    print(True)
if 'pepperoni' in requested_topping:
    print(False)


# Проверка отсутсвия значения в списке not

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(user.title() + " , you can post a responce if you wish.")


# Логические выражения

game_active = True
can_edit = False

# Простые команды if

age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

# Программы if -else

age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")


# Цепочки if- elif-else
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10")

# компактное выполнение кода верхней цепочки if - elif - else
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print("Your admission cost is $" + str(price) + ".")

# Серии блоков elif

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5

print("Your admission cost is $" + str(price) + ".")

# Отсутсвие блока else

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5

print("Your admission cost is $" + str(price) + ".")


# Проверка нескольких условий

requested_topping = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_topping:
    print("Adding mushrooms.")
if 'pepperoni' in requested_topping:
    print("Adding pepperoni.")
if 'extra cheese' in requested_topping:
    print("Adding extra cheese")

print("\nFinished making your pizza!")

# Проверка специавльных значений

requested_toppings = ['mushrooms', ' green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")



requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")


print("\nFinished making your pizza!")


# Проверка наличия элементов в списке

requested_toppings_2 = []

if requested_toppings_2:
    for requested_topping in requested_toppings_2:
        print("Adding " + requested_topping + ".")
        print("\nFinished making your pizza!")
    else:
        print("Are you sure you want a plain pizza?")


# Множественные списки

available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings_3 = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings_3:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza!")