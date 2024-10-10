import numpy as np

import matplotlib.pyplot as plt

data = np.loadtxt('Lab1/PersonalTask1/output.txt', skiprows=1, delimiter=':')

x = data[:, 0]  # Первая колонка

y1 = data[:, 1]  # Вторая колонка

y2 = data[:, 2]  # Третья колонка

# Создаем фигуру и оси для графиков

plt.figure(figsize=(10, 5))

# Строим график y1(x)

plt.subplot(1, 2, 1)  # 1 строка, 2 колонки, график 1

plt.plot(x, y1, label='y1(x)', color='blue')

plt.title('График y1(x)')

plt.xlabel('x')

plt.ylabel('y1')

plt.grid(True)

plt.legend()

# Строим график y2(x)

plt.subplot(1, 2, 2)  # 1 строка, 2 колонки, график 2

plt.plot(x, y2, label='y2(x)', color='orange')

plt.title('График y2(x)')

plt.xlabel('x')

plt.ylabel('y2')

plt.grid(True)

plt.legend()

# Показываем графики в одном окне

plt.tight_layout()  # Удобное распределение графиков

plt.show()

