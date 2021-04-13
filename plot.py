import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
import numpy as np

x = np.arange(-10, 10, 0.1)
y = np.sin(x)

fig, ax = plt.subplots()

ax.plot(x,y)

x1 = np.arange(-10, 10, 0.2)
for i in range(len(x1)):
    y1 = np.sin(x1[i])
    y2 = np.sin(x1[i] + 0.2)
    y0 = y2
    if np.abs(y1) <= np.abs(y2):
        y0 = y1
    if(y1 * y2 <= 0):
        y0 = 0
    ax.add_patch(patches.Rectangle((x1[i], 0), 0.2, y0, fill = False ,alpha = 1))

annotationText = "Illustration of \n$\int_{a}^{b} sin(x) dx$"
ax.text(0.1, .65, annotationText, transform=ax.transAxes, fontsize=9, verticalalignment='top')

plt.xlim([-0.75, 2])
plt.ylim([-0.8, 1.1])

ax.xaxis.set_ticks_position('both')
ax.yaxis.set_ticks_position('both')

ax.xaxis.set_major_locator(MultipleLocator(0.4))
ax.xaxis.set_minor_locator(MultipleLocator(0.2))
ax.yaxis.set_major_locator(MultipleLocator(0.2))
ax.yaxis.set_minor_locator(MultipleLocator(0.1))

ax.tick_params(which = 'major', axis='both', direction='in', length=6, width=1)
ax.tick_params(which = 'minor', axis='both', direction='in', length=3, width=0.5)

ax.set_aspect(1.0/ax.get_data_ratio(), adjustable = 'box')

#plt.grid()

ax.set_title("Integration of Sine-Wave Over X")
ax.set_xlabel("x-axis (radian)")
ax.set_ylabel("y-axis")

plt.show()
