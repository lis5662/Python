# Создание и использование классов

class Dog():
    """Простая модель собаки."""
    def __init__(self, name, age):
        """Инициализирует атрибуты name и age."""
        self.name = name
        self.age = age

    def sit(self):
        """Собака садится по команде."""
        print(self.name.title() + " is now sitting.")
    def roll_over(self):
        """Собака перекатывается п окоманде."""
        print(self.name.ttile() + " rolled over!")


# Создание экземпляра

#class Dog():
    ...
#    my_dog = Dog('willie', 6)
#    my_dog.sit()
#    my_dog.roll_over()
#    print("My dog's name is " + my_dog.name.title() + ".")
#    print("My dog is " + str(my_dog.age) + " years old.")

# Создание нескольких экземпляров

#class Dog():
    ...

#    my_dog = Dog('willie', 6)
#    your_dog = Dog('lucy', 3)

#    print("My dog's name is " + my_dog.name.title() + ".")
#    print("My dog is " + str(my_dog.age) + " years old.")
#    my_dog.sit()

#    print("\nYour dog's name is " + your_dog.name.title() + ".")
#    print("Your dog is " + str(your_dog.age) + " years old.")
#    your_dog.sit()


# Класс Car

class Car():
    """Простая модель автомобиля."""

    def __init__(self, make, model, year):
        """Инициализирует артибуты описания автомобиля"""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Возвращает аккуратно отформатированное описание."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

# Назначение атрибуту значения по умолчанию

class Car():
    """Простая модель автомобиля."""

    def __init__(self, make, model, year):
        """Инициализирует артибуты описания автомобиля"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Возвращает аккуратно отформатированное описание."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Выводит пробег машины в милях."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """Устанавливает заданное значение на одометре.
        При попытке обратной подкрутки изменения отклоняются."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Увеличивает показания одометра с заданным приращением."""
        self.odometer_reading += miles



my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# Прямое изменение значения атрибута
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# Изменение атрибута с помощью метода
my_new_car.update_odometer(23)
my_new_car.read_odometer()

my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()


# Нааследование

class Car():
    """Прсотая модель автомобиля."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):
    """Представляет аспекты машины, специфические для электромобилей"""
    def __init__(self, make, model, year):
        """Инициализирует атрибуты класса-родителя.
        Затем инициализирует артибуты, специфические для электромобиля."""
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def fill_gas_tank():
        """У электромобиля нет бензобака."""
        print("This car doesn't need a gas tank!")

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()


# Экземпляры как атрибуты

class Battery():
    """Простая модель аккумулятора электромобиля."""

    def __init__(self, battery_size=70):
        """Инициализирует атрибуты аккумулятора."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Выводит приблизительный запас хода от аккумулятора"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)


class ElectricCar(Car):
    """Представляет аспекты машины, специфические для электромобилей"""
    def __init__(self, make, model, year):
        """Инициализирует атрибуты класса-родителя.
        Затем инициализирует артибуты, специфические для электромобиля."""
        super().__init__(make, model, year)
        self.battery = Battery()

        my_tesla = ElectricCar('tesla', 'model s', 2016)

        print(my_tesla.get_descriptive_name())
        my_tesla.battery.describe_battery()
        my_tesla.battery.get_range()

# Стандартная библиотека python

from collections import OrderedDict
favorite_languages = OrderedDict()
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
              language.title() + ".")