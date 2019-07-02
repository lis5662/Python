# Работа со списками  цикл for

magicians = ['alice', 'david', 'carolina']
for magicians in magicians:
    print(magicians)


# Более сложные действия с циклом for

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")


# Выполнение действий после цикла for

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

print("Thank you, everyone. That was a great magic show!")


# Создание числовых списков range(), list()

for value in range(1, 5):
    print(value)

# Создание списка из вызывающихся чисел

numbers = list(range(1, 6))
print(numbers)

# Построение четных чисел even

even_numbers = list(range(2, 11, 2))
print(even_numbers)

# создание списка квадратов всех целых чисел

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

# компактный вариант

squares = []
for value in range(1, 11):
    squares.append(value**2)

print(squares)

# Простая статистика с числовыми списками min(), max(), sum()

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))          # выводит минимальное значение списка
print(max(digits))          # выводит максимальное значение списка
print(sum(digits))          # выводит сумму значений списка


# Генераторы списокв

squares = [value ** 2 for value in range(1, 11)]
print(squares)


# Работа с частью списка - срезы

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])


players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])


players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4])


players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:])


# перебор содержимого среза

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())


# Копирование списка

my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]

my_foods.append('cannoli')
friends_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friends_foods)


# Кортежи

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#dimensions[0] = 250 нельзя присваивать новое значение в кортеже

# перебор всех значений в кортеже

dimensions = (200,50)
for dimension in dimensions:
    print(dimension)

# замена кортежа

dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)




