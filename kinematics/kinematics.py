import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create an empty numpy array to hold scatter points
points = np.empty((0,3))

# Add scatter points to the array
points = np.append(points, [[0,0,0], [0.101,0.055,0], [0.101,0.11,0]], axis=0)
points = np.append(points, [[0.0126,0.11,-0.0884], [0.108,0.11,-0.1838]], axis=0)

# Create a 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(points[:,0], points[:,1], points[:,2])

# Set axis labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title('3D Scatter Plot')

# Show the plot
plt.show()
