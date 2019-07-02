# Определение фнукции

def greet_user():
   """Выводит простое приветствие."""
print("Hello!")

greet_user()

# Передача информации функции

def greet_user(username):
    """Выводит простое приветствие."""
    print("Hello, " + username.title() + "!")

greet_user('jesse')


# Аргументы и параметры

# Позиционнаые аргументы

def describe_pet(animal_type, pet_name):
    """Выводит информацию о животном."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')

# Многократные вызовы функции

def describe_pet(animal_type, pet_name):
    """Выводит информацию о животном"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# Именованный аргумент

def describe_pet(animal_type, pet_name):
    """Выводит информацию о животном"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(animal_type='hamster', pet_name='harry')



# Значения по умолчанию

def describe_pet(pet_name,animal_type= 'dog'):
    """Выводит информацию о животном"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='willie')


# Эквивалентные вызовы функции

describe_pet('willie')
describe_pet(pet_name='willie')

describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')



# Возвращение простого значения

def get_formatted_name(first_name, last_name):
    """Возвращает аккуратно отформатированное полное имя."""
    full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)


# Необязательные аргументы

def get_formatted_name(first_name, middle_name, last_name):
    """Возвращает аккуратно отформатированное полное имя."""
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'lee', 'hendrix')
print(musician)


def get_formatted_name(first_name, last_name, middle_name=''):
    """Возвращает аккуратно отформатированное полное имя."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)


# Возваршение словаря

def build_person(first_name, last_name):
    """Возвращает словарь с информацией о человеке."""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)



def build_person(first_name, last_name, age=''):
    """Возвращает словарь с информацией о человеке."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)


# Использование функции в цикле while

def get_formatted_name(first_name, last_name):
    """Возвращает аккуратно отформатированное полное имя."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

# Бесконечный цикл!

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")


# Передача списка

def greet_uesrs_1(names_1):
    """Вывод простого приветсвтвия для каждого пользователя в списке"""
    for name in names_1:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames_2 = ['hannah', 'ty', 'margot']
greet_uesrs_1(usernames_2)


# Изменение списка в функции

# список моделей, которые необходимо напечатать
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Цикл последовательно печатает каждую модель до конца списка.
# После печати каждая модель перемещается в список completed models
while unprinted_designs:
    current_design = unprinted_designs.pop()
    # Печать модели на 3D- принтере.
    print("Printing model: " + current_design)
    completed_models.append(current_design)

    # Вывод всех готовых моделей
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)



# Две функции

def print_models(unprinted_designs, completed_models):
    """
    Имитирует печать моделей, пока список не станет пустым.
    Каждая ммодель после печати перемещается в completed_models.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

    # Имитация печати модели на 3D- принтере.
    print("Printing model: " + current_design)
    completed_models.append(current_design)

def show_completed_models(completed_models):
    """Выводит информацию обо всех напечатанных моделях."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# Передача произвольного набора аргументов

def make_pizza(*toppings):
    """Вывод списка заказанных дополнений"""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


def make_pizza(*toppings):
    """Выводит описание пиццы."""
    print("\nMaking a pizza with the following toppings: ")
    for topping in toppings:
        print("- " + topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


# Позиционнные аргументы с произвольными наборами  аргументов

def make_pizza(size,*toppings):
    """Выводит описание пиццы."""
    print("\nMaking a " + str(size) + " + inch pizza with the following toppings: ")
    for topping in toppings:
        print("- " + topping)

make_pizza(16, 'pepperoni')
make_pizza( 12, 'mushrooms', 'green peppers', 'extra cheese')


# Использование произвольного набора именованных аргументов

def build_profile(first, last, **user_info):
    """Строит словарь с информацией о пользователе."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',
                             location= 'princeton',
                             field= 'physics')
print(user_profile)



# Хранение функций в модулях

def make_pizza(size, *toppings):
    """Выводит описание пиццы."""
    print("'\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

