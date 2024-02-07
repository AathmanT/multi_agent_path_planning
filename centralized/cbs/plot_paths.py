import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

from cbs.constants import PLT_OBSTACLE_RADIUS, PLT_ROBOT_RADIUS


def plot_map_and_paths(data, paths):
    # Increase the size of the plot
    fig, ax = plt.subplots(figsize=(10, 10))

    # Set the dimensions of the plot based on the map dimensions
    ax.set_xlim([-1, data['map']['dimensions'][0] + 1])
    ax.set_ylim([-1, data['map']['dimensions'][1] + 1])

    # Draw grid
    ax.set_xticks(np.arange(0, data['map']['dimensions'][0], 1))
    ax.set_yticks(np.arange(0, data['map']['dimensions'][1], 1))
    plt.grid()

    # Plot the agents
    for agent in data['agents']:
        start = patches.Circle((agent['start'][0] + 0.5, agent['start'][1] + 0.5), radius=PLT_ROBOT_RADIUS, color='blue')
        goal = patches.Circle((agent['goal'][0] + 0.5, agent['goal'][1] + 0.5), radius=PLT_OBSTACLE_RADIUS, color='green')
        ax.add_patch(start)
        ax.add_patch(goal)

    # Plot the obstacles
    for obstacle in data['map']['obstacles']:
        obs = patches.Circle((obstacle[0] + 0.5, obstacle[1] + 0.5), radius=PLT_OBSTACLE_RADIUS, color='red')
        ax.add_patch(obs)

    # Plot the paths
    for agent, path in paths.items():
        # Unzip the path into X and Y coordinates
        X, Y = zip(*[(state.location.x + 0.5, state.location.y + 0.5) for state in path])
        # Plot the path with a line
        ax.plot(X, Y, color='black', alpha=0.5)
        # Plot the circles
        for state in path:
            location = state.location
            circle = patches.Circle((location.x + 0.5, location.y + 0.5), radius=PLT_ROBOT_RADIUS, facecolor='yellow', alpha=0.5)
            ax.add_patch(circle)

    # plt.show()
    plt.show(block=False)  # Display the figure without blocking
    plt.pause(4)  # Pause for 5 seconds and then close the figure
    plt.close()  # Close the figure
