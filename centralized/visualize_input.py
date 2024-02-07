#!/usr/bin/env python3
import yaml
import matplotlib
# matplotlib.use("Agg")
from matplotlib.patches import Circle, Rectangle, Arrow
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
import matplotlib.animation as manimation
import argparse
import math
from pyvirtualdisplay import Display


import matplotlib.pyplot as plt
import matplotlib.patches as patches
from examples.multi_agent_path_planning.centralized.cbs.constants import PLT_OBSTACLE_RADIUS, PLT_ROBOT_RADIUS


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("map", help="input file containing map")
  # parser.add_argument("schedule", help="schedule for agents")
  parser.add_argument('--video', dest='video', default=None, help="output video file (or leave empty to show on screen)")
  parser.add_argument("--speed", type=int, default=1, help="speedup-factor")
  args = parser.parse_args()


  with open(args.map) as map_file:
    data = yaml.load(map_file, Loader=yaml.FullLoader)

  # Increase the size of the plot
  fig, ax = plt.subplots(figsize=(10, 10))

  # Set the dimensions of the plot based on the map dimensions
  ax.set_xlim([-1, data['map']['dimensions'][0] + 1])
  ax.set_ylim([-1, data['map']['dimensions'][1] + 1])

  # Draw grid
  ax.set_xticks(np.arange(0, data['map']['dimensions'][0], 1))
  plt.xticks(rotation='vertical')
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

  plt.show()

