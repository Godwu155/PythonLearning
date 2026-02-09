import matplotlib.pyplot as plt
from RandomWalk import *


rw = RandomWalk()
rw.generate()

plt.style.use("classic")
fig,ax = plt.subplots(figsize=(16,9))

point_numbers = range(rw.num_points)

# ax.scatter(rw.x_values, rw.y_values,c=point_numbers,cmap = 'Blues',edgecolors='none',s=1)
ax.plot(rw.x_values, rw.y_values, color='red', label='Random Walk',linewidth=1)
ax.set_aspect("equal")

ax.scatter(0,0,c='green',edgecolors='none',s=10)
ax.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=10)

ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)

plt.show(dpi=500)