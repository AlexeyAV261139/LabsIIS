import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Определяем диапазон значений x и y
x = np.arange(-2, 2, 0.1)
y = np.arange(-2, 2, 0.1)
x, y = np.meshgrid(x, y)

# Определяем функцию
z = np.exp(x) * np.sin(-x**2 - y**2)

# Создаем 3D-график
figure = plt.figure(figsize=(7,5))
axes = figure.add_subplot(111, projection='3d')
axes.plot_surface(x, y, z, cmap='viridis')

# Добавляем линии уровня
contour = axes.contour(x, y, z, zdir='z', offset=np.min(z), cmap='viridis')

# Настраиваем график
axes.set_xlabel('X')
axes.set_ylabel('Y')
axes.set_zlabel('f(X, Y)')
axes.set_title('3D график функции f(x, y) и линии уровня')

plt.colorbar(contour)
plt.show()