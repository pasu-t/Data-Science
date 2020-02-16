import numpy as np
import matplotlib.pyplot as plt

columns = ['A', 'B', 'C', 'D']
rows = ['1', '2', '3', '4']

data = np.random.random((4,4))

fig = plt.figure()

ax = fig.add_subplot(111)

cax = ax.matshow(data, interpolation='nearest')
fig.colorbar(cax)

ax.set_xticklabels([''] + columns)
ax.set_yticklabels([''] + rows)

plt.show()
