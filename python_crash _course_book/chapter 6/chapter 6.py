# Простой словарь

alien_0 = {'color' : 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])


# Работа со словарями

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")


# Добавление новых пар ключ-значение

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['x_position'] = 25
print(alien_0)


# Создание пустого словаря

alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)


# Изменение значений в словаре

alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")


alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))
# Пришелец перемещается в право.
# Вычисляем величину смещения на основании текущей скорости

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # Пришелец двигается быстро
    x_increment = 3
# Новая позиция равна сумме старой позиции и приращения.

alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x position: " + str(alien_0['x_position']))


# Удаление пар ключ-значение

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)


# Слоаврь с однотипными обьектами

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("Sarah's favotire language is " +
      favorite_languages['sarah'].title() +
      ".")


# Перебор всех пар ключ-значение

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)



favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title() + ".")


# Перебор всех ключей в словаре

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name in favorite_languages.keys():
    print(name.title())



favorite_languages_1 = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

friends = ['phil', 'sarah']
for user_name in favorite_languages_1.keys():
    print(user_name.title())

if user_name in friends:
    print("  Hi " + user_name.title() +
          ", I see your favorite language is " +
          favorite_languages_1[user_name].title() + "!")



favorite_languages_2 = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

if 'erin' not in favorite_languages_2.keys():
    print("Erin, please take our poll!")


# Упорядоченный перебор ключей

favorite_languages_3 = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name in sorted(favorite_languages_3.keys()):
    print(name.title() + ", thank you for talking the poll.")



# Перебор всех значений в словаре - values()


favorite_languages_4 = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("The following languages have been mentioned:")
for language in favorite_languages_4.values():
    print(language.title())




# Множества set

favorite_languages_4 = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("The following languages have been mentioned:")
for language in set(favorite_languages_4.values()):
    print(language.title())


# Список словарей

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# Создание пустого списка для хранения пришельцев
aliens = []

# Создание 30 зеленых пришельцев

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Вывод первых 5 пришельцев:
for alien in aliens[:5]:
    print(alien)
print("...")

# Вывод количества созданных данных пришельцев
print("Totla number of aliens: " + str(len(aliens)))


# Создание пустого списка для хранения пришельцев
aliens = []

# Создание 30 зеленых пришельцев

for alien_number in range(0, 30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# Вывод первых 5 пришельцев

for alien in aliens[0:5]:
    print(alien)
    print("...")


# Сохранение информации о заказанной пицце

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# Описание заказа
print("You ordered a " + pizza['crust'] + " -crust pizza " +
      "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)



favorite_languages_5 = {
    'jen': ['python', 'ruby'],
    'sarah':['c'],
    'edward':['ruby', 'go'],
    'phil': ['python', 'haskell'],
}


for name, languages in favorite_languages_5.items():
    if len(languages):
        print("\n" + name.title() + "'s favorite languages are:")

for language in languages:
        print("\t" + language.title())



# Словарь в словаре

users = {
    'aeinstein':{
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },

}

for username_2, user_info in users.items():
    print("\nUsername: " + username_2)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())



