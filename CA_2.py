import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the function f(x, y)
def f(x, y):
    return x**2 + y**2 + 3*x + 4*y + 5

# Generate x and y values
x = np.linspace(-3, 1, 400)
y = np.linspace(-3, 1, 400)
x, y = np.meshgrid(x, y)
z = f(x, y)
# Minimum point coordinates
min_x = -1.5
min_y = -2.0
min_z = f(min_x, min_y)
# Create a 3D plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
# Plot the surface
ax.plot_surface(x, y, z, cmap='viridis', alpha=0.8)
# Highlight the minimum point
ax.scatter(min_x, min_y, min_z, color='red', s=100, label=f"Min at ({min_x}, {min_y}, {min_z})")
# Set labels
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('f(x, y)')
# Add a legend
ax.legend()
# Show the plot
plt.show()
