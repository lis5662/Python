# 8-1

#def display_message():
#    """Выводите простое значение"""
#    print("I'm learning functions from this chapter of the book!")

#display_message()


# 8-2

#def favorite_book(title):
#    """Выводит название любимой книги"""
#    print("My favorite book is " + title.title() + "!")

#favorite_book('Python crash course')


# 8-3

def make_shirt(size, text):
    print("T-shirt size is: " + size.title() + ".")
    print("T-shirt text is: " + text.title() + ".")

make_shirt('Large', 'Good for nothing')
make_shirt(text='Large', size='Good for nothing')

# 8-4

def make_shirt(l, text):
    print("T-shirt size is: " + l.title() + ".")
    print("T-shirt text is: " + text.title() + ".")

make_shirt('Large', 'I love Python!')
make_shirt(l='Large', text='I love Python!')
make_shirt('Medium', 'I love Python!')


# 8-5

def describe_city(city, country='usa'):
    """Выводим Название городов и стран в 2 аргумента"""
    print(city.title() + " is in " + country.upper() + ".")

describe_city('Los Angeles', country='usa')
describe_city('Boston', country='usa')
describe_city('Toronto', country='canada')


# 8-6

def city_country(city, country):
    """Возврашает строку для города и страны"""
    city_func = city + "," + ' ' + country + "."
    return city_func.title()

city_country_1 = city_country('\nLos Angeles', 'California')
print(city_country_1)

city_country_1 = city_country('Rome', 'Italy')
print(city_country_1)

city_country_1 = city_country('Kiev', 'Ukraine')
print(city_country_1)


# 8-7

def make_album(artist_name, album_name, track=''):
    """Выводит данные из словаря имя группы и название альбома"""
    music = {'artist': artist_name, 'album': album_name}
    if track:
        music['track'] = track
        return music

musician = make_album('Killswitch Engage', 'The End of Heartache', track='Take This Oath')
musician_1 = make_album('Soilwork', 'Stabbing theDrama', track='Nerve')
musician_2 = make_album('In Flames', 'Come Clarity', track='Take This Life')
print(musician)
print(musician_1)
print(musician_2)

# 8-8

def make_album(artist_name, album_name):
    """Выводит данные из словаря имя группы и название альбома"""
    music = artist_name + ' ' + album_name
    return music.title()

while True:
    print("\nPlease enter artist and album names here: ")
    print("(enter 'q' at any time to quit)")

    art_name = input("Enter artist name: ")
    if art_name == 'q':
        break
    alb_name = input("Enter album name: ")
    if alb_name == 'q':
        break

    album_name = make_album(art_name, alb_name)
    print("\nYour information: " + album_name + "!")


# 8-9


def show_magicians(magicians):
    """Вывод простого приветсвтвия для каждого пользователя в списке"""
    for name in show_magicians():
        msg = "Hello, " + name.title() + "!"
        print(msg)

magic = ['hannah', 'walter', 'margot']
print(magic)


# 8-10

def show_magicians(magicians):
    """Print the name of each magician in the list."""
    for magician in magicians:
        print(magician)

def make_great(magicians):
    """Add 'the Great!' to each magician's name."""
    # Build a new list to hold the great musicians.
    great_magicians = []

    # Make each magician great, and add it to great_magicians.
    while magicians:
        magician = magicians.pop()
        great_magician = magician + ' the Great'
        great_magicians.append(great_magician)

    # Add the great magicians back into magicians.
    for great_magician in great_magicians:
        magicians.append(great_magician)

magicians = ['Harry Houdini', 'David Blaine', 'Teller']
show_magicians(magicians)

print("\n")
make_great(magicians)
show_magicians(magicians)



# 8 -11

def show_magicians(magicians):
    """Print the name of each magician in the list."""
    for magician in magicians:
        print(magician)

def make_great(magicians):
    """Add 'the Great!' to each magician's name."""
    # Build a new list to hold the great musicians.
    great_magicians = []

    # Make each magician great, and add it to great_magicians.
    while magicians:
        magician = magicians.pop()
        great_magician = magician + ' the Great'
        great_magicians.append(great_magician)

    # Add the great magicians back into magicians.
    for great_magician in great_magicians:
        magicians.append(great_magician)

    return magicians

magicians = ['Harry Houdini', 'David Blaine', 'Teller']
show_magicians(magicians)

print("\nGreat magicians:")
great_magicians = make_great(magicians[:])
show_magicians(great_magicians)

print("\nOriginal magicians:")
show_magicians(magicians)


# 8-12

def make_sandwich(*sandwiches):
    """Вывод списка сендвичей."""
    print("\nI'll make you a great sandwich:")
    for item in sandwiches:
        print(" ...adding " + item + " to your sandwich.")
    print("Your sandwich is ready")


make_sandwich('roast beef', 'cheddar cheese', 'lettuce', 'honey dijon')
make_sandwich('turkey', 'apple slices', 'honey mustard')
make_sandwich('peanut butter', 'strawberry jam')


# 8-13

def build_profile(first, last, **user_info):
    """Строит словарь с информацией о пользователе."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('dima', 'doronin',
                             location= 'kharkov',
                             field= 'programming')
print(user_profile)

# 8-14

def make_car(manufacturer, model, **options):
    """Строит функцию с названиями автомобилей"""
    new_car ={'manufacturer': manufacturer.title(),
              'model': model.title()}

    for option, value in options.items():
        new_car[option] = value
    return new_car

my_outback = make_car('subaru', 'outback', color='blue', tow_package=True)
print(my_outback)

my_accord = make_car('honda', 'accord', year=1991, color='white',
                     headlights='popup')
print(my_accord)



