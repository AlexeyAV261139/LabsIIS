import numpy as np
import matplotlib.pyplot as plt

# Задаем диапазон и шаг
x = np.arange(-np.pi, np.pi, 0.1)

# Определяем функцию
f = np.sin(x) + 0.3 * np.cos(7 * x)

# Построение графиков с разными маркерами и цветами
plt.plot(x, f, marker='o', color='r', label='Красный с кругами')
plt.plot(x, f, marker='s', color='g', label='Зеленый с квадратами')
plt.plot(x, f, marker='x', color='b', label='Синий с крестами')

# Добавление заголовка, легенды и осей
plt.title('График f(x) = sin(x) + 0.3 * cos(7 * x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()

# Показ графика
plt.grid(True)
plt.show()
