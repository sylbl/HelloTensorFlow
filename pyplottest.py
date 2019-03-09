import numpy as np
import matplotlib.pyplot as plt

x_data = np.random.rand(100)
y_data = x_data * 0.1 + 0.3

plt.title("y=0.1x+0.3")
plt.scatter(x_data, y_data)
plt.show()
