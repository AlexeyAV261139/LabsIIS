import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Чтение данных из файла
data = np.loadtxt('clust5.dat')

# Разделение данных на x (доход), y (возраст), z (кредит)
x = data[:, 0]  # доход
y = data[:, 1]  # возраст
z = data[:, 2]  # кредит

# Расчет математических ожиданий
Mx = np.mean(x)
My = np.mean(y)
Mz = np.mean(z)

# Создание 3D-графика
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Построение поля точек
ax.scatter(x, y, z, c='b', marker='o', label='Клиенты')

# Построение точки с координатами (Mx, My, Mz)
ax.scatter(Mx, My, Mz, c='r', marker='o', s=100, label='Мат. ожидание')

# Подписи осей
ax.set_xlabel('Доход (тыс. руб.)')
ax.set_ylabel('Возраст (лет)')
ax.set_zlabel('Кредит (тыс. руб.)')
ax.set_title('Поле точек')

# Показ легенды
ax.legend()

# Отображение графика
plt.show()

# Сортировка данных по возрасту (y)
sorted_data = data[data[:, 1].argsort()]

# Запись отсортированных данных в новый файл
np.savetxt('sorted_clust5.dat', sorted_data, fmt='%.2f')
