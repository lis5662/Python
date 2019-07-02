# Упражнения словари


# 6-1

dict = {
    'first_name': 'Olya',
    'last_name': 'Doronina',
    'age': 27,
    'city': 'Kharkov',
                  }

print(dict)

print("My wife name is " + dict['first_name'] + ".")
print("Her last name is " + dict['last_name'] + ".")
print("She is " + str(dict['age'])+ " years old.")
print("She lives in " + dict['city'] + ".")


# 6-2

dict_2 = {
    'Olya': 23,
    'Dima': 7,
    'Andrey': 27,
    'Alexander': 3,
                  }

print("Olya favorite number is " + str(dict_2['Olya']) + ".")
print("Dima favorite number is " + str(dict_2['Dima']) + ".")
print("Andrey favorite number is " + str(dict_2['Andrey']) + ".")
print("Alexander favorite number is " + str(dict_2['Alexander']) + ".")


# 6-3

glossary = {
        'if-elif-else': 'Условная инструкция - основной инструмент выбора в Python. '
                        'Проще говоря, она выбирает, какое действие следует выполнить, '
                        'в зависимости от значения переменных в момент проверки условия. ',
        'цикл for': 'Цикл for уже чуточку сложнее, чуть менее универсальный, '
                    'но выполняется гораздо быстрее цикла while.' \
                    ' Этот цикл проходится по любому итерируемому объекту (например строке или списку), '
                    'и во время каждого прохода выполняет тело цикла.',
        'списки list': 'Списки в Python - упорядоченные изменяемые коллекции объектов произвольных типов'
                       ' (почти как массив, но типы могут отличаться).',
        'кортежи tuple': 'Кортеж, по сути - неизменяемый список.',
        'словари dict': 'Словари в Python - неупорядоченные коллекции произвольных объектов с доступом по ключу.'
                        ' Их иногда ещё называют ассоциативными массивами или хеш-таблицами.',
}

print("Условная инструкция if-elif-else: \n" + glossary['if-elif-else'])
print("Условная инструкция Цикл for: \n" + glossary['цикл for'])
print("Условная инструкция списки list: \n" + glossary['списки list'])
print("Условная инструкция кортежи tuple: \n" + glossary['кортежи tuple'])
print("Условная инструкция словари dict: \n" + glossary['словари dict'])


# 6-4

glossary_2 = {
        'if-elif-else': 'Условная инструкция - основной инструмент выбора в Python. '
                        'Проще говоря, она выбирает, какое действие следует выполнить, '
                        'в зависимости от значения переменных в момент проверки условия. ',
        'цикл for': 'Цикл for уже чуточку сложнее, чуть менее универсальный, '
                    'но выполняется гораздо быстрее цикла while.' \
                    ' Этот цикл проходится по любому итерируемому объекту (например строке или списку), '
                    'и во время каждого прохода выполняет тело цикла.',
        'списки list': 'Списки в Python - упорядоченные изменяемые коллекции объектов произвольных типов'
                       ' (почти как массив, но типы могут отличаться).',
        'кортежи tuple': 'Кортеж, по сути - неизменяемый список.',
        'словари dict': 'Словари в Python - неупорядоченные коллекции произвольных объектов с доступом по ключу.'
                        ' Их иногда ещё называют ассоциативными массивами или хеш-таблицами.',
        'числа': 'Числа в Python 3 ничем не отличаются от обычных чисел. '
                 'Они поддерживают набор самых обычных математических операций:',
        'множества': 'Множество в python - "контейнер", содержащий не повторяющиеся элементы в случайном порядке.',
}


for key, values in glossary_2.items():
    print("\nKey: " + key)
    print("Value: " + values)


# 6-5

rivers = {
    'nile': 'egypt',
    'amazon': 'South America',
    'Yangtze': 'Asia',
    'Mississippi': 'USA',
}

for river, country in rivers.items():                                 # выводим ключи и значения
    print("The " + river.title() + " runs through " + country.title() + ".")

for river in rivers.keys():                                           # Выводим только ключи
    print(river.title())


for country in rivers.values():                                           # Выводим только значения
    print(country.title())



# 6-6


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



# 6-7

dict_d = {
    'wife':{
        'first_name': 'Olya',
        'last_name': 'Doronina',
        'city': 'Kharkov',
    },
    'husband': {
        'first_name': 'Dima',
        'last_name': 'Doronin',
        'city': 'Kharkov',
    },
    'cat':{
        'first_name': 'Richard',
        'last_name': 'Dan',
        'city': 'Kharkov',
    },
}

for username, userinfo in dict_d.items():
    print("\nUsername: " + username)
    full_name = userinfo['first_name'] + " " + userinfo['last_name']
    city = userinfo['city']
    print("\tFull name: " + full_name.title())
    print("\tCity: " + city.title())


# 6-8

animals = {
    'cat1':{
        'breed': 'Scottish Straight',
        'owner_name': 'Olya',
    },
    'cat2': {
        'breed': 'Persian',
        'owner_name': 'Dima',
    },
    'cat3':{
        'breed': 'Siamese',
        'owner_name': 'Kuzya',
    },
}

for cat_breed, animal_info in animals.items():
    print("\nCat breed: " + cat_breed)
    owner_name1 = animal_info['breed']
    owner = animal_info['owner_name']
    print("\tInformation: " + owner_name1.title())
    print("\tOwner name: " + owner.title())


# 6-9

favorite_places = {
    'dima':{
        'place1': 'usa',
        'place2': 'canada',
    },
    'olya':{
        'place1': 'spain',
        'place2': 'italy',
    },
    'katya':{
        'place1': 'germany',
        'place2': 'france',
    },
}

for place, city in favorite_places.items():
    print("\nName: " + place)
    places = city['place1']
    places_2 = city['place2']
    print("\tFirst favorite place: " + places.title())
    print("\tSecond favorite place: " + places_2.title())



# 6-10

dict_3 = {
    'Olya':{
        'value1': 23,
        'value2': 22,
    },
    'Dima':{
        'value1': 7,
        'value2': 8,
    },
    'Max':{
        'value1': 11,
        'value2': 2,
    },
    'Alex':{
        'value1': 33,
        'value2': 21,
    },
}

for val, name in dict_3.items():
    print("\nName: " + val)
    values1 = name['value1']
    values2 = name['value2']
    print("\tFirst favorite value: " + str(values1))
    print("\tSecond favorite value: " + str(values2))


# 6-11

cities = {
    'New York':{
        'country': 'usa',
        'population': 20000000,
        'fact': 'beautiful city!',
    },
    'Boston':{
        'country': 'usa',
        'population': 10000000,
        'fact': 'beautiful city!',
    },
    'Toronto':{
        'country': 'canada',
        'population': 10000000,
        'fact': 'beautiful city!',
    },
    'Los Angeles':{
        'country': 'usa',
        'population': 30000000,
        'fact': 'beautiful city!',
    },
}

for city_1, info in cities.items():
    print("\nCity name: " + city_1)
    info_1 = info['country']
    info_2 = str(info['population'])
    info_3 = info['fact']
    print("\tCountry name: " + info_1)
    print("\tCity population " + str(info_2))
    print("\tCity fact " + info_3)



# 6-12

cities_2 = {
    'New York': {
        'country': 'usa',
        'population': 20000000,
        'fact': 'beautiful city!',
    },
    'Boston': {
        'country': 'usa',
        'population': 10000000,
        'fact': 'beautiful city!',
    },
    'Toronto': {
        'country': 'canada',
        'population': 10000000,
        'fact': 'beautiful city!',
    },
    'Los Angeles': {
        'country': 'usa',
        'population': 30000000,
        'fact': 'beautiful city!',
    },
}

for city_3, info in cities_2.items():
    print("\nCity name: " + city_3)
    info_1 = info['country']
    info_2 = str(info['population'])
    info_3 = info['fact']
    print("\tCountry name: " + info_1)
    print("\tCity population " + str(info_2))
    print("\tCity fact " + info_3)



