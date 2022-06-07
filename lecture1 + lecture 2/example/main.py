import matplotlib.pyplot as plt
from math import sin, cos

pi = 3.141592

x = []
num = 10000
for i in range(num):
    x.append(2 * pi / num * i)

y_sin = [sin(d) for d in x]
y_cos = [cos(d) for d in x]

fig, ax = plt.subplots()

ax.plot(x, y_sin, label="sin(x)")
ax.plot(x, y_cos, label="cos(x)")

ax.set_title("Гармонические функции")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()

plt.show()