# 3-1

friend_names = ['Alexander', 'Max', 'Dil', 'Alexey', 'Dorf']
print(friend_names[0])
print(friend_names[1])
print(friend_names[2])
print(friend_names[3])
print(friend_names[4])

# 3-2

friend_names = ['New York - Alexander',
                'California - Max',
                'Texas - Dil',
                'Colorado - Alexey',
                'Alaska - Dorf']
print("Hello my friends from" ", "
      + friend_names[0] + ", "
      + friend_names[1] + ", "
      + friend_names[2] + ", "
      + friend_names[3] + ", "
      + friend_names[4]
      )

# 3-3

cars = ['Nissan GTR', 'Acura MDX', 'Infiniti QX', 'BMW X5']
print("I wan't to buy a new", cars[0])
print("I wan't to buy a new", cars[1])
print("I wan't to buy a new", cars[2])
print("I wan't to buy a new", cars[3])


# 3-4

guests = []

guests.append("Adriano")
guests.append("Maria")
guests.append("Roberto")

print("Hi " + guests[0] + " i invite you to dinner" + ".")
print("Hi " + guests[1] + " i invite you to dinner" + ".")
print("Hi " + guests[2] + " i invite you to dinner" + ".")


# 3-5

guests = []

guests.append("Adriano")
guests.append("Maria")
guests.append("Roberto")
print(guests[0] + " will not be able to come to dinner")


popped_adriano = guests.pop(0)
guests.insert(0, "Ugo")

print(guests[0] + " came instead of " + popped_adriano + " for lunch " + ".")
print("Hi " + guests[1] + " i invite you to dinner" + ".")
print("Hi " + guests[2] + " i invite you to dinner" + ".")


# 3-6

guests = []

guests.append("Adriano")
guests.append("Maria")
guests.append("Roberto")
print(guests[0] + " will not be able to come to dinner")


popped_adriano = guests.pop(0)
guests.insert(0, "Ugo")

print(guests[0] + " came instead of " + popped_adriano + " for lunch " + ".")
print("Hi " + guests[1] + " i invite you to dinner" + ".")
print("Hi " + guests[2] + " i invite you to dinner" + ".")

print("We bought a new table and we had 3 more places for lunch.")

guests.insert(0, "Monica")
guests.insert(1, "Antonio")
guests.append("Hullio")

print(guests)

print("Hi " + guests[0] + " i invite you to dinner" + ".")
print("Hi " + guests[1] + " i invite you to dinner" + ".")
print("Hi " + guests[2] + " i invite you to dinner" + ".")
print("Hi " + guests[3] + " i invite you to dinner" + ".")
print("Hi " + guests[4] + " i invite you to dinner" + ".")
print("Hi " + guests[5] + " i invite you to dinner" + ".")


# 3-7

guests = []

guests.append("Adriano")
guests.append("Maria")
guests.append("Roberto")
print(guests[0] + " will not be able to come to dinner")


popped_adriano = guests.pop(0)
guests.insert(0, "Ugo")

print(guests[0] + " came instead of " + popped_adriano + " for lunch " + ".")
print("Hi " + guests[1] + " i invite you to dinner" + ".")
print("Hi " + guests[2] + " i invite you to dinner" + ".")

print("We bought a new table and we had 3 more places for lunch.")

guests.insert(0, "Monica")
guests.insert(1, "Antonio")
guests.append("Hullio")

print(guests)

print("Hi " + guests[0] + " i invite you to dinner" + ".")
print("Hi " + guests[1] + " i invite you to dinner" + ".")
print("Hi " + guests[2] + " i invite you to dinner" + ".")
print("Hi " + guests[3] + " i invite you to dinner" + ".")
print("Hi " + guests[4] + " i invite you to dinner" + ".")
print("Hi " + guests[5] + " i invite you to dinner" + ".")

print("We are sorry but we can only invite two people.")

print(guests.pop(5) + "," + " we are sorry that we can not invite you to dinner")
print(guests.pop(4) + "," + " we are sorry that we can not invite you to dinner")
print(guests.pop(3) + "," + " we are sorry that we can not invite you to dinner")
print(guests.pop(2) + "," + " we are sorry that we can not invite you to dinner")

print(guests[0] + " and " + guests[1] + " only you are invited for dinner" + ".")
del guests[1]
del guests[0]
print(guests)


# 3-8


countries = ['USA',
             'Great Britain',
             'Canada',
             'Australia',
             'Indonesia']
print(countries)
print(sorted(countries))
print(countries)
print(sorted(countries, reverse=True))
print(countries)
countries.reverse()
print(countries)
countries.reverse()
print(countries)
countries.sort()
print(countries)
countries.sort(reverse=True)
print(countries)



# 3-9


guests = []

guests.append("Adriano")
guests.append("Maria")
guests.append("Roberto")
guests.append("Umberto")
print(len(guests))


# 3-10

games_list = ["World of Warcraft", "Warcraft 3", "Risen", "Gothic", "The Elder Scrolls"]

games_list.append("Max Payne")
print(games_list)
last_game = games_list.pop()
print(last_game)
games_list.remove("Risen")
print(games_list)
del games_list[0]
print(games_list)
games_list.sort()
print(games_list)
games_list.sort(reverse=True)
print(games_list)
print(sorted(games_list))
games_list.reverse()
print(games_list)
print(len(games_list))
games_list.append("Metro 2033")
games_list.append("Fallout")
print(games_list)
expensive_game = games_list.pop(1)
print("This game " + expensive_game + " is too expensive for my budget!")

last_game = "Fallout"
games_list.remove("Fallout")
print("\nThis is not what i wan't " + last_game + ".")


# 3-11

films = []

films.append("Game of the Thrones")
films.append("The Lord of the Rings")
films.append("Luther")
print(films[-2])