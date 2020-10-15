import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-10,10,0.1)
y = np.cos(x)
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_title('δ(n)')
plt.xlabel('x')
plt.ylabel('y')
ax1.scatter(x, y, c='b', marker='o')
plt.legend('x1')
plt.show()