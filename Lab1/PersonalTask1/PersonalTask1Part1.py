import numpy as np

a = 0       # Начало отрезка
b = 10      # Конец отрезка
h = 0.1     # Шаг

# Создание и открытие файла для записи
with open('Lab1/PersonalTask1/output.txt', 'w') as f:
    f.write("x, y1, y2\n")  # Заголовок для файла

    # Вычисления для каждого x в заданном диапазоне
    x = a
    while x <= b:
        y1 = np.sin(x**2) * np.cos(5*x)  # Вычисление y1
        y2 = np.cos(np.sin(9.2*x))        # Вычисление y2
        f.write(f"{x:.2f}:{y1:.6f}:{y2:.6f}\n")  # Запись значений в файл
        x += h  # Увеличиваем x на шаг h