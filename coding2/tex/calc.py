import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the range
x = np.linspace(3, 7, 200)
y = x**3

# Create a meshgrid for rotation
theta = np.linspace(0, 2 * np.pi, 200)
X, T = np.meshgrid(x, theta)

# f(x)^2 rotated = y = x^3 → radius
Y = (X**3) * np.cos(T)
Z = (X**3) * np.sin(T)

# Plot
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, Z, color='mediumslateblue', alpha=0.8, rstride=5, cstride=5, linewidth=0)

# Labels
ax.set_title(r"Solid of Revolution: $f(x)=x^3$ from $x=3$ to $x=7$", fontsize=14)
ax.set_xlabel("x-axis")
ax.set_ylabel("y-axis")
ax.set_zlabel("z-axis")

plt.tight_layout()
plt.show()