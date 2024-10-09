import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Определяем диапазон значений x и y
x = np.arange(-2, 2, 0.1)
y = np.arange(-2, 2, 0.1)

# Создаем сетку значений
X, Y = np.meshgrid(x, y)

# Вычисляем значения функции f
Z = np.exp(X) * np.sin(-X**2 - Y**2)

# Создаем 3D график
fig = plt.figure(figsize=(12, 6))

# 3D график поверхности
ax = fig.add_subplot(121, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_title('3D Graph of f(x,y) = e^x * sin(-x^2 - y^2)')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

# Линии уровня
contour = fig.add_subplot(122)
contour.contour(X, Y, Z, levels=20, cmap='viridis')
contour.set_title('Contour Plot of f(x,y)')
contour.set_xlabel('X axis')
contour.set_ylabel('Y axis')

plt.tight_layout()
plt.show()