import numpy as np
import matplotlib.pyplot as plt

# Define the function f(x)
def f(x):
    sum_squares = (x * (x + 1) * (2 * x + 1)) / 6
    return 0.5 * sum_squares**2

# x values (positive integers)
x = np.arange(1, 1000000, 1)

# Compute f(x)
y = f(x)

# Plot it
plt.figure(figsize=(10, 6))
plt.plot(x, y, label=r'$f(x) = \frac{1}{2} \left(\sum_{i=1}^{x} i^2\right)^2$', color='darkorange')
plt.title("Plot of $f(x) = \\frac{1}{2} \\left(\\sum_{i=1}^{x} i^2\\right)^2$")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()