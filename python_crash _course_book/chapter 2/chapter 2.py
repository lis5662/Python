# Переменные и простые типы данных

message = "Hello Python World!"
print(message)

message = "Hello Python Crash Course World!"
print(message)


car = "Nissan"
model = "Rogue"
engine = "2.5"
transmission = "CVT"

print("My car is", car, ". " "Model of my car is", model, ". " "Engine of my car is", engine, ". " "Transmission of my car is", transmission)


# Строки

name = "ada lovelace"
print(name.title())                 # первая буква все слов строки становится в верхнем регистре

name = "ada lovelace"
print(name.upper())                 # все буквы строки в верхнем регистре

name = "ada lovelace"
print(name.lower())                 # все буквы строки в нижнем регистре


# Конкатенация

first_name = "ada"
last_name = "lovecase"
full_name = first_name + " " + last_name
print(full_name)

print("Hello, " + full_name.title() + "!")

message = "Hello, " + full_name.title() + "!"

print(message)


# Табуляции и разрывы строк

print("\tPython")           # табуляция
print("Languages: \nPython\nC\nJavaScript")     # разрыв строки


print("Languages:\n\tPython\n\tC\n\tJavaScript") # Разбиение на 4 строки


favorite_language = 'python '
favorite_language = favorite_language.rstrip() # удаление пробела у правого края
print(favorite_language)

favorite_language = 'python '
favorite_language.lstrip()              # удаление пробела у левого края
favorite_language.rstrip()              # удаление пробелов с двух сторон


# Предотвращение синтаксически хошибок в строках

message = "One of Python's strenghts is its diverse community."
print(message)


# Числа

a = 3 * 0.1
print(a)

age = 23
message_age = "Happy " + str(age) + "rd Birthday!"
print(message_age)




