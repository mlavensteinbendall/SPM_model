# import numpy as np
# import matplotlib.pyplot as plt

# # Load data from the text file with space delimiter
# data = np.loadtxt('ds_convergence/test_0.txt')

# # Assuming each column represents a solution and each row represents a time step
# num_solutions = data.shape[1]

# # Create a time array (assuming time steps are consecutive integers)
# time_steps = np.arange(data.shape[0])

# # Plot each solution over time
# for i in range(num_solutions):
#     plt.plot(time_steps, data[:, i], label=f'Solution {i + 1}')

# # Add labels and legend
# plt.xlabel('Time Step')
# plt.ylabel('Solution Value')
# plt.legend()
# plt.title('Solution Over Time')

# # Show the plot
# plt.show()


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Load data from the text file with space delimiter
data = np.loadtxt('ds_convergence/test_0.txt')

# Assuming each column represents a solution and each row represents a time step
num_solutions = data.shape[1]
num_time_steps = data.shape[0]

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlabel('Time Step')
ax.set_ylabel('Solution Value')
ax.set_title('Solution Over Time')

# Create line objects for each solution
lines = [ax.plot([], [], label=f'Solution {i + 1}')[0] for i in range(num_solutions)]
ax.legend()

# Function to initialize the plot
def init():
    for line in lines:
        line.set_data([], [])
    return lines

# Function to update the plot for each frame
def update(frame):
    for i, line in enumerate(lines):
        line.set_data(np.arange(frame + 1), data[:frame + 1, i])
    return lines

# Create the animation
animation = FuncAnimation(fig, update, frames=num_time_steps, init_func=init, blit=True)

# Save the animation as a GIF using Pillow (instead of imagemagick)
animation.save('solution_over_time.gif', writer='pillow', fps=10)

# Show the plot (optional)
plt.show()
