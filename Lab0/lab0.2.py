import numpy as np
import matplotlib.pyplot as plt

# Задаем диапазон для первой функции
x1 = np.linspace(1e-3, 1e3, 1000)
y1 = -np.arctan(5*x1) - np.arctan(2*x1)

# Задаем диапазон для третьей функции
x2 = np.linspace(-10, 10, 1000)
y2 = np.sin(x2**2)

# Создание подокон с тремя графиками
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# 1-е подокно: обычный график функции
axs[0].plot(x1, y1)
axs[0].set_title('График y = -arctg(5x) - arctg(2x)')
axs[0].set_xlabel('x')
axs[0].set_ylabel('y')

# 2-е подокно: линейный масштаб Y, логарифмический X
axs[1].plot(x1, y1)
axs[1].set_xscale('log')
axs[1].set_title('График с логарифмическим X')
axs[1].set_xlabel('log(x)')
axs[1].set_ylabel('y')

# 3-е подокно: график sin(x^2)
axs[2].plot(x2, y2)
axs[2].set_title('График sin(x^2)')
axs[2].set_xlabel('x')
axs[2].set_ylabel('sin(x^2)')

# Отображение графиков
plt.tight_layout()
plt.show()
