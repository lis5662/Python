# 5-1

car = 'acura'
if car == 'acura':
    print("This is True")
    print(car == 'acura')
    print("My car is " + car.upper())

car = 'nissan'
if car != 'mazda':
    print("This is not True")
    print(car != 'nissan')
    print("My car is not a " + car.upper())


# 5-2

# Проверка равенства и неравенства строк
car = 'lexus'
if car == 'lexus':
    print(True)

# Проверка с ипользованием функции lower()
if car.lower() == 'Lexus':
    print(True)
else:
    print(False)

# Числовые проверки
year = 360
days = 350
if days > year:
    print(True)
else:
    print(False)

if days < year:
    print(True)
else:
    print(False)

if days >= year:
    print(True)
else:
    print(False)

if days <= year:
    print(True)
else:
    print(False)


# Проверки с ключевым словом and и or

year = 360
days = 350
if days > year and days <= year:
    print(True)
else:
    print(False)

if days > year or days <= year:
    print(True)
else:
    print(False)


# Проверка вхождения элемента в список in

cars = ['mazda', 'audi', 'dodge']
if 'lexus' in cars:
    print("This is True answer!")
else:
    print("This is False answer!")

# Проверка отсутсвия элемента в списке not in

cars = ['mazda', 'audi', 'dodge']
car = 'lexus'
if car not in cars:
    print("This is True answer!")
else:
    print("This is False answer!")


# 5-3

alien_color = 'green'

if alien_color == 'green':
    print("You got 5 points!")
if alien_color == 'red':
    print("The color does not match!")


# 5-4

alien_color = 'yellow'

if alien_color == 'yellow':
    print("You got 5 points!")
else:
    print("You got 10 points!")



# 5-5

alien_color = 'red'

if alien_color == 'green':
    print("You got 5 points!")
elif alien_color == 'yellow':
    print("You got 10 points!")
elif alien_color == 'red':
    print("You got 15 points!")



# 5-6

age = 28

if age < 2:
    print("Младенец")
elif (age >= 4) and (age < 13):
    print("Ребенок")
elif (age <= 13) and (age < 20):
    print("подросток")
elif (age >= 20) and (age < 65):
    print("Взрослый")
elif age >= 65:
    print("Пожилой")
else:
    print("Наслаждайтесь жизнью, возраст не важен!")


# 5-7

favorite_fruits = ['peach', 'mango', 'bananas']

if 'peach' in favorite_fruits:
    print("You really like " + favorite_fruits[0].upper() + "!")
if 'mango' in favorite_fruits:
    print("You really like " + favorite_fruits[1].upper() + "!")
if 'bananas' in favorite_fruits:
    print("You really like " + favorite_fruits[2].upper() + "!")
if 'papaya' not in favorite_fruits:
    print("You don't really like " + favorite_fruits[0].upper() + "!")
if 'coconut' not in favorite_fruits:
    print("You don't really like " + favorite_fruits[1].upper() + "!")
if 'orange' not in favorite_fruits:
    print("You don't really like " + favorite_fruits[2].upper() + "!")


# 5-8

names = ['Alex', 'Max', 'Dima', 'Olya', ' Andrey', 'admin']

for name in names:
    if name == 'Alex':
        print("Hello, " + names[0] + " thank you for logging in again")
    elif name == 'Max':
        print("Hello, " + names[1] + " thank you for logging in again")
    elif name == 'Dima':
        print("Hello, " + names[2] + " thank you for logging in again")
    elif name == 'Olya':
        print("Hello, " + names[3] + " thank you for logging in again")
    elif name == 'Andrey':
        print("Hello, " + names[4] + " thank you for logging in again")
    elif name == 'admin':
        print("Hello, " + names[5] + " would you like to see a status report?")



# 5-9

names2 = []

if 'Alex' not in names2:
    print("We need to find some users")
    for name in names2:
        if name == 'Alex':
            print("Hello, " + names2[0] + " thank you for logging in again")
        elif name == 'Max':
            print("Hello, " + names2[1] + " thank you for logging in again")
        elif name == 'Dima':
            print("Hello, " + names2[2] + " thank you for logging in again")
        elif name == 'Olya':
            print("Hello, " + names2[3] + " thank you for logging in again")
        elif name == 'Andrey':
            print("Hello, " + names2[4] + " thank you for logging in again")
        elif name == 'admin':
            print("Hello, " + names2[5] + " would you like to see a status report?")
        else:
            print("We need to find some users")


# 5-10

current_users = ['Alex', 'Max', 'Dima', 'Olya', ' Andrey', 'admin']
new_users = ['Alex', 'John', 'Jason', 'Richard', 'Gustavo', 'admin']

for users in new_users:
    if users in current_users:
        print("You must choose another name " + users.lower())



# 5-11

values = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

for val in values:
    if val == '1':
        print(values[0] + "st")
    elif val == '2':
        print(values[1] + "nd")
    elif val == '3':
        print(values[2] + "rd")
    elif val == '4':
        print(values[3] + "th")
    elif val == '5':
        print(values[4] + "th")
    elif val == '6':
        print(values[5] + "th")
    elif val == '7':
        print(values[6] + "th")
    elif val == '8':
        print(values[7] + "th")
    elif val == '9':
        print(values[8] + "th")
    else:
        print("Empty")

        # Упрощенный вариант ???

        values_1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

        for val_1 in values_1:
            if val_1 in values_1:
                print(values_1[0] + "st\n" + values_1[1] + "nd\n" + values_1[2] + "rd\n"
                      + values_1[3] + "th\n" + values[4] + "th\n" + values[5] + "th\n"
                      + values[6] + "th\n" + values[7] + "th\n" + values[8] + "th")

