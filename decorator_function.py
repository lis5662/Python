from datetime import date, datetime
from functools import wraps

# Создаем функцию декоратор
def find_time_for_execute(func):
    @wraps(func)
    def cover(*args, **kwargs):
        start = datetime.now()
        my_current_age = func(*args, **kwargs)
        before_20000_days = 20000 - int(my_current_age)
        end = datetime.now()
        print(f"Функция {func.__name__} выполнялась {end - start} секунд")
        print(f"До 20000 дней мне осталось: {before_20000_days}")
    return cover

@find_time_for_execute
def my_age_in_days(year: int, month: int, day: int):
    birthday = date(year, month, day)
    today = date.today()
    delta = today - birthday
    return delta.days

# my_age_in_days(1990, 9, 23)



