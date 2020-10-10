import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-5.0, 5.0, 0.01)
y1 = np.sin(x)/x
plt.figure(1)
plt.subplot(211)
plt.plot(x, y1)
plt.show()