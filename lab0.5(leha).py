import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Функция для расчёта f(x)
def f(x, d, k):
    return d * x + k * np.random.uniform(0, 1, len(x))

# Функция для вычисления СКО
def CKO(k, d):
    x = np.arange(0, 10, 0.1)  # значения x на отрезке [0, 10]
    f_values = f(x, d, k)  # вычисляем значения функции f(x)
    mx = np.mean(f_values)  # математическое ожидание
    N = len(x)  # количество точек
    e = np.sqrt(np.sum((f_values - mx)**2) / (N - 1))  # вычисляем СКО по формуле (1)
    return e

# Диапазон изменения параметров k и d
k_values = np.arange(1, 9, 0.1)
d_values = np.arange(1, 9, 0.1)

# Подготовка сетки для параметров k и d
K, D = np.meshgrid(k_values, d_values)
E = np.zeros_like(K)  # Массив для хранения СКО

# Вычисление СКО для каждого сочетания k и d
for i in range(len(k_values)):
    for j in range(len(d_values)):
        E[j, i] = CKO(k_values[i], d_values[j])

# Построение 3D-графика
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Создание 3D поверхности
ax.plot_surface(K, D, E, cmap='viridis')

# Настройки осей
ax.set_xlabel('k')
ax.set_ylabel('d')
ax.set_zlabel('СКО e(k, d)')
ax.set_title('График зависимости СКО e(k, d)')

# Отображение графика
plt.show()

# Теперь создаем подпрограмму для функции Z(x, y)
def Z(x, y):
    if -5 <= x <= 5 and 0 <= y <= 7:
        return 14
    elif (x - 13)**2 + (y - 13)**2 <= 5:
        return 7
    elif (x + 13)**2 + (y + 15)**2 <= 6:
        return 9
    else:
        return 0

# Диапазон изменения x и y
x_values = np.linspace(-20, 20, 100)
y_values = np.linspace(-20, 20, 100)

# Подготовка сетки для функции Z(x, y)
X, Y = np.meshgrid(x_values, y_values)
Z_values = np.zeros_like(X)

# Вычисление значений Z(x, y)
for i in range(len(x_values)):
    for j in range(len(y_values)):
        Z_values[j, i] = Z(x_values[i], y_values[j])

# Построение 3D-графика для Z(x, y)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Создание 3D поверхности
ax.plot_surface(X, Y, Z_values, cmap='plasma')

# Настройки осей
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('Z(x, y)')
ax.set_title('График функции Z(x, y)')

# Отображение графика
plt.show()
