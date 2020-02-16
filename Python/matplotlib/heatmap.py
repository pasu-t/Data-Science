import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import numpy as np

np.random.seed(1)
a = np.random.random((25, 25))

plt.subplot(1, 1, 1)
plt.pcolor(a, norm=LogNorm(vmin=a.min() / 1.2, vmax=a.max() * 1.2), cmap='PuBu_r')
plt.colorbar()

plt.show()
