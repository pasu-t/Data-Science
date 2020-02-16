from matplotlib import pyplot as plt
import numpy as np

x = [5,10,20,25]
y = [5,10,20,25]

hist, xedges, yedges = np.histogram2d(x,y)
X,Y = np.meshgrid(xedges,yedges)
plt.imshow(hist)
plt.grid(True)
plt.colorbar()
plt.show()

# # using pcolor
# plt.pcolor(hist)
# plt.colorbar()
# plt.grid()
# plt.show()
