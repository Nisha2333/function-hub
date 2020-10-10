import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-100.0, 100.0, 0.01)
y1 = np.exp(0.01*x)*np.cos(x)
plt.figure(1)
plt.subplot(211)
plt.plot(x, y1)
plt.xlabel('t')
plt.ylabel('x(t)')
plt.show()