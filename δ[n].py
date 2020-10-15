import numpy as np
import matplotlib.pyplot as plt
def function(x):
    y = x == 0
    return y.astype(np.int)
x = np.arange(-10, 10)
y = function(x)
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_title('δ(n)')
plt.xlabel('x')
plt.ylabel('y')
ax1.scatter(x, y, c='b', marker='o')
plt.legend('x1')
plt.grid(True)
plt.show()