#message = input("Tell me something, and I will repeat ir back to you: ")
#print(message)

# Содержатильные подсказки
#name = input("Please enter your name: ")
#print("Hello, " + name + "!")


#promt = "If you tell us who you are, we can personalize the messages you see."
#promt += "\nWhat is your first name? "

#name = input(promt)
#print("\nHello, " + name + "!")


# использование int()

#age = input("How old are you? ")
#print(age)

#height = input("How tall are you, in inches? ")
#height = int(height)

#if height >= 36:
#    print("\nYou're tall eough to ride!")
#else:
#    print("\nYou'll be able to ride when you're a little older.")


# Оператор вычисления остатка %

#number = input("Enter a number, and I'll tell you if it's even or odd: ")
#number = int(number)

#if number % 2 == 0:
#    print("\nThe number " + str(number) + " is even.")
#else:
#    print("\nThe number " + str(number) + " is odd.")



# Циклы while

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# Пользователь пытается прервать программу

promt = "\nTell me something, and I will repeat it back to you:"
promt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(promt)
    print(message)

if message != 'quit':
    print(message)


# Флаги

promt = "\nTell me something, and I will repeat it back to you:"
promt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(promt)

    if message == 'quit':
        active = False
    else:
        print(message)

# break

promt = "\nPlease enter the name of a city you have visited:"
promt += "\n(Enter 'quit' when you are finished.)"

while True:
    city = input(promt)

    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")


# Команда continue

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)


# Предотвращение зацикливания

x = 1
while x <= 5:
    print(x)
    x += 1


# Использование циклов while со списками и словарями

# Начинаем с двух списков:
# и пустого списка для хранения проверенных пользователей
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Проверяем каждого пользователя , пока остаются непроверенные
# пользователи. Каждый пользователь, прошедший проверку,
# перемещается в список проверенных.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

# Вывод всех проверенных пользователей.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# Удаление всех вхождений конкретного значения из списка

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)


# Заполнение словаря данными, введенными пользователем

responses = {}

# Установка флага продолжения опроса.
polling_active = True

while polling_active:
    # Запрос имени и ответа пользователя.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Ответ сохраняется в словаре:
    responses[name] = response

    # Првоерка продолжения опроса.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active =False

    # Опрос завершен, вывести результаты.
    print("\n--- Poll Results ---")
    for name, response in responses.items():
        print(name + " would like to climb " + response + ".")
