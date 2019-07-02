# 7-1

# car_list = ['audi q7', 'nissan murano', 'infiniti q50', 'bmw x5']

# print("I want rent some of yours car. Can you help me please?")
# car_rent = input("\nWhat car you want for rent?: "  + car_list[2] + "\nDo you have this car?")
# print(car_rent)


# car = input("Car for rent:")
# print("Let me see if I can find you a " + car + "!")


# 7-2

# cafe = input("Рow many places do you want to book a table: ")
# cafe = int(cafe)

# if cafe >= 8:
#    print("You need to wait!")
# else:
#    print("The table is ready!")


# 7-3

# num = int(input("Enter your number here: "))

# if num % 10 == 0:
#    print("\nThe number " + str(num) + " is a multiple of 10")
# else:
#    print("The number " + str(num) + " not a multiple of 10")


# 7-4

# promt = "\nPlease enter the toppings for pizza:"
# promt += "\n(Enter 'quit' when you are finished.)"

# while True:
#    toppings = input(promt)

#    if toppings == 'quit':
#        break
#    else:
#        print("I'd like add " + toppings.title() + " to the pizza!")


# 7-5

#tickets = input("\nEnter your age here: ")
#tickets = int(tickets)
#while tickets:
#    if tickets <= 3:
#        print("Free ticket!")
#        break
#    elif tickets <= 12:
#        print("Ticket price is $10")
#        break
#    elif tickets > 12:
#        print("Ticket price is $15")
#        break

# 7-6

#promt = "\nPlease enter the toppings for pizza:"
#promt += "\n(Enter 'quit' when you are finished.)"

#active = True
#while active:
#    toppings = input(promt)

#    if toppings == 'mushrooms':
#        continue
#    elif toppings == 'quit':
#        active = False
#        break
#    else:
#        print("I'd like add " + toppings.title() + " to the pizza!")

# 7-7

#engine = 5.7
#while True:
#    engine += 1
#    print(engine)

# 7-8

sandwich_orders = ['fish sandwich', 'chicken sandwich', 'vegan sandwich', 'meat sandwich']
finished_sandwiches = []

while sandwich_orders:
    current_order = sandwich_orders.pop()

    print("I made you " + current_order.title() + " sandwich" + ".")
    finished_sandwiches.append(current_order)

    print("Your list of cooked sandwiches: ")
    for finished_sandwich in finished_sandwiches:
        print(finished_sandwich.title())


# 7-9

print("We no longer have pastrami")
sandwich_orders = ['pastrami', 'chicken sandwich', 'pastrami', 'pastrami', 'pineapple sandwich']
print(sandwich_orders)

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)


# 7-10

# Заполнение словаря данными, введенными пользователем

responses = {}

# Установка флага продолжения опроса.
polling_active = True

while polling_active:
    # Запрос имени и ответа пользователя.
    name = input("\nWhat is your name? ")
    response = input("Where would you like to spend your vacation? ")

    # Ответ сохраняется в словаре:
    responses[name] = response

    # Првоерка продолжения опроса.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active =False

    # Опрос завершен, вывести результаты.
    print("\n--- Poll Results ---")
    for name, response in responses.items():
        print(name + " would like to spend your vacation in " + response + ".")

