bicycles = ['trek', 'cannondle', 'redline', 'specialized']
print(bicycles[0].title())
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])


bicycles = ['trek', 'cannondle', 'redline', 'specialized']
message = "My first bcycles was a " + bicycles[0].title() + "."
print(message)

# Изменение элементов списка

cars = ['Nissan GTR', 'Acura MDX', 'Infiniti QX', 'BMW X5']
print(cars)

cars[0] = 'Honda Accord'
print(cars)

# присоединение жлементов в конце списка

cars = ['Nissan GTR', 'Acura MDX', 'Infiniti QX', 'BMW X5']
print(cars)

cars.append("Acura RDX")
print(cars)


cars = []

cars.append("Honda")
cars.append("Volvo")
cars.append("Audi")
cars.append("Toyota")
print(cars)


# Вставка элементов в список

cars = ['Nissan GTR', 'Acura MDX', 'Infiniti QX', 'BMW X5']
print(cars)

cars.insert(0, "Audi Q8")
print(cars)

# Удаление из списка del

cars = ['Nissan GTR', 'Acura MDX', 'Infiniti QX', 'BMW X5']
print(cars)

del cars[0]
print(cars)

# удаление с помощью pop()

cars = ['Nissan GTR', 'Acura MDX', 'Infiniti QX', 'BMW X5']
print(cars)

last_owned = cars.pop()
print("The last car I owned was a " + last_owned.title() + ".")


# Извлечение элементов из произвольного списка pop()

cars = ['Nissan GTR', 'Acura MDX', 'Infiniti QX', 'BMW X5']
first_owned = cars.pop(0)
print("The first car I owned was a " + first_owned.title() + ".")

# Удаление элемента по значению remove()

cars = ['Nissan GTR', 'Acura MDX', 'Infiniti QX', 'BMW X5']
print(cars)

cars.remove('Acura MDX')
print(cars)


cars = ['Nissan GTR', 'Acura MDX', 'Infiniti QX', 'BMW X5']
print(cars)
too_exprensive = "BMW X5"
cars.remove(too_exprensive)
print(cars)
print("\n " + too_exprensive.title() + " is too exprensive for me.")


# Упорядочение списка

# sort()
cars = ['dodge', 'chevrolet', 'lexus', 'subaru']
cars.sort()                                        # Список сортируется в алфавитном порядке
print(cars)


cars = ['dodge', 'chevrolet', 'lexus', 'subaru']
cars.sort(reverse=True)                          # Список сортируется в обратном порядке
print(cars)

# Временная сортировка списка sorted()

cars = ['dodge', 'chevrolet', 'lexus', 'subaru']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")                                                  # Список сортируется временно
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)


# Вывод списка в обратном порядке

cars = ['dodge', 'chevrolet', 'lexus', 'subaru']
cars.reverse()                          # Список сортируется в обратном порядке
print(cars)

# Определение длины списка len()

cars = ['dodge', 'chevrolet', 'lexus', 'subaru']
print(len(cars))



# Ошибки вывода списков

films = []

films.append("Game of the Thrones")
films.append("The Lord of the Rings")
films.append("Luther")
print(films[-1])