# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 10)
y = np.sin(x)
plt.plot(x, y)
plt.show()
plt.plot(x, y)
plt.slabel("Time")
plt.xlabel("Time")
plt.ylabel("Some function of time")
plt.title("My cool chart")
plt.show()
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.show()
