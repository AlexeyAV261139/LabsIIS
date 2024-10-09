import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-np.pi, np.pi, 0.1)
f_x = np.sin(x) + 0.3 * np.cos(7 * x)

plt.figure(figsize=(10, 6))
plt.plot(x, f_x, marker='o', color='blue', label='sin(x) + 0.3cos(7x)', linestyle='-')

plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')

plt.title('График функции f(x) = sin(x) + 0.3cos(7x)')
plt.legend()
plt.show()