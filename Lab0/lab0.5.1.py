import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Определяем диапазоны для k и d
k_values = np.arange(1, 9.1, 0.1)
d_values = np.arange(1, 9.1, 0.1)

# Создаем сетку для значений k и d
K, D = np.meshgrid(k_values, d_values)

# Задаем диапазон для x
x = np.arange(0, 10.1, 0.1)

# Инициализируем массив для СКО
std_dev = np.zeros_like(K)

# Вычисляем СКО для каждой пары (k, d)
for i in range(K.shape[0]):
    for j in range(K.shape[1]):
        k = K[i, j]
        d = D[i, j]
        # Генерируем случайные числа
        rand = np.random.uniform(0, 1, len(x))
        # Вычисляем функцию f(x)
        f_x = d * x + k * rand
        # Вычисляем СКО
        std_dev[i, j] = np.std(f_x)

# Создаем 3D график
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(K, D, std_dev, cmap='viridis')

# Настраиваем метки осей
ax.set_xlabel('k')
ax.set_ylabel('d')
ax.set_zlabel('СКО(e(k,d))')
ax.set_title('Зависимость СКО от параметров k и d')

# Показываем график
plt.show()
