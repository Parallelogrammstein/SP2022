import matplotlib.pyplot as plt
import numpy as np
import csv


x1 = []
x2 = []
y1 = []
y2 = []

x = np.linspace(-4.5, 1.5, 1000)
y = x ** 2 + 3 * x - 4

with open("bd-dec21-births-deaths-natural-increase.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        t_var = row["Births_Deaths_or_Natural_Increase"]
        if t_var == "Births":
            x1.append(int(row["Period"]))
            y1.append(int(row["Count"]))
        elif t_var == "Deaths":
            x2.append(int(row["Period"]))
            y2.append(int(row["Count"]))

fig, axs = plt.subplots(1, 2)

axs[0].plot(x1, y1, label="birth level")
axs[0].plot(x2, y2, label="death level")
axs[0].set_title("Birth and death count")
axs[0].set_xlabel("year")
axs[0].set_ylabel("amount")
axs[0].legend()

axs[1].plot(x, y, label="x^2 + 3x - 4")
axs[1].set_title("Parabola")
axs[1].set_xlabel("x")
axs[1].set_ylabel("y")
axs[1].legend()

plt.show()