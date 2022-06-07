import matplotlib.pyplot as plt
import numpy as np


x1 = np.linspace(0, 2, 1000)
y1 = 2 ** x1 + 4 ** (x1 ** 2)
x2 = np.linspace(0, 2, 1000)
y2 = 3 ** x2 + 3 ** (x2 ** 2)

fig, ax = plt.subplots()

ax.plot(x1, y1)
ax.plot(x2, y2, color="green")

plt.show()