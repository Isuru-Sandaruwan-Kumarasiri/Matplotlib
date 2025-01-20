import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 10, 0.1)
y_1 = x
y_2 = np.sqrt(x)
y_3 = np.power(x, 2)
y_4 = np.power(x, 3)

plt.figure()  # Create a new figure

# First subplot: y = x
plt.subplot(2, 2, 1)  # Divide figure into 2 rows, 2 columns, chart #1
plt.plot(x, y_1, 'ro')  # Red circles
plt.title("y = x")

# Second subplot: y = sqrt(x)
plt.subplot(2, 2, 2)  # Divide figure into 2 rows, 2 columns, chart #2
plt.plot(x, y_2, 'g--')  # Green dashed line
plt.title("$y = \\sqrt{x}$")  # LaTeX for square root

# Third subplot: y = x^2
plt.subplot(2, 2, 3)  # Divide figure into 2 rows, 2 columns, chart #3
plt.plot(x, y_3, 'b^')  # Blue triangles
plt.title("$y = x^2$")  # LaTeX for x squared

# Fourth subplot: y = x^3
plt.subplot(2, 2, 4)  # Divide figure into 2 rows, 2 columns, chart #4
plt.plot(x, y_4, 'ks')  # Black squares
plt.title("$y = x^3$")  # LaTeX for x cubed

# Display the plot
plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()
