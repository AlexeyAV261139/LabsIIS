import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return -np.arctan(5 * x) - np.arctan(2 * x)

x = np.linspace(1e-3, 1e3, 400)

fig, axs = plt.subplots(3, 1, figsize=(10, 10))

axs[0].plot(x, f(x))
axs[0].set_title('График функции y = -arctg(5*x) - arctg(2*x)')
axs[0].set_xlabel('x')
axs[0].set_ylabel('y')
axs[0].grid()

axs[1].semilogx(x, f(x))
axs[1].set_title('Логарифмический масштаб по оси X')
axs[1].set_xlabel('x (логарифмический)')
axs[1].set_ylabel('y')
axs[1].grid()

x2 = np.linspace(0, 10, 400)

axs[2].plot(x2, np.sin(x2**2))
axs[2].set_title('График функции y = sin(x^2)')
axs[2].set_xlabel('x')
axs[2].set_ylabel('y')
axs[2].grid()

plt.tight_layout()
plt.show()