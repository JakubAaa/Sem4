import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))


x = np.linspace(start=-3, stop=3, num=50)
y = np.exp(-x**2)
y_err = np.random.normal(loc=np.mean(y), scale=0.1, size=len(y))

ax[0].plot(x, y, marker='o', label="exp(-x^2)")
ax[0].fill_between(x, y - y_err, y + y_err, alpha=0.2, label="+/- szum")

ax[0].set_xlabel("x")
ax[0].set_ylabel("y")
ax[0].legend(loc="upper left")


x = np.arange(start=-50.0, stop=50.0, step=0.1)
y_1 = np.cos(x / 3.0)
y_2 = np.sin(x)

ax[1].plot(x, y_1, label="cos(x/3)")
ax[1].plot(x, y_2, label="sin(x)")

ax[1].set_xscale('symlog')
ax[1].grid(which='both')

ax[1].set_xlabel("x")
ax[1].set_ylabel("y")
ax[1].legend(loc="lower right")

fig.suptitle("Funkcje wygenerowane w 'numpy' i wykreślone w 'matplotlib'")
plt.savefig("moj_wykres.png")
