import matplotlib.pyplot as plt

# Вывод серии точек функцией scatter()
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.scatter(x_values, y_values, s=100)

# Автоматическое вычисление данных
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c=y_values,cmap=plt.cm.Blues, edgecolor='none', s=40)

# Назначение диапозона для каждой оси
plt.axis([0, 1100, 0, 1100000])


plt.scatter(2, 4, s=200)

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)

# Назначение заголовка диаграммы и меток осей.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Назначение размера шрифта делений на осях.
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()

