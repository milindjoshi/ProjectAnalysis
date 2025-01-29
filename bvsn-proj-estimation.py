import numpy as np
import matplotlib.pyplot as plt
import configparser
import os

# Create a config file structure
config = configparser.ConfigParser()

# Write to a config file
config_path = '/users/milin/programs/JiraAnalysis/project_config.ini'

# Read constants from the config file
config = configparser.ConfigParser()
config.read(config_path)

# Extract project parameters
sprint_duration_weeks = int(config['PROJECT']['sprint_duration_weeks'])
velocity = int(config['PROJECT']['velocity'])
#print(f'velocity: {velocity}')
num_resources = int(config['PROJECT']['num_resources'])
hours_per_week_per_resource = int(config['PROJECT']['hours_per_week_per_resource'])
non_project_hours = int(config['PROJECT']['non_project_hours'])
story_points_per_hour = float(config['PROJECT']['story_points_per_hour'])

# Extract backlog data
groomed_story_points = int(config['BACKLOG']['groomed_story_points'])
ungroomed_story_count = int(config['BACKLOG']['ungroomed_story_count'])
avg_story_points_per_story = int(config['BACKLOG']['avg_story_points_per_story'])

# Extract simulation parameters
simulations = int(config['SIMULATION']['simulations'])
velocity_std_dev = float(config['SIMULATION']['velocity_std_dev'])

# Derived values
working_hours_per_week = hours_per_week_per_resource - non_project_hours
ungroomed_story_points = ungroomed_story_count * avg_story_points_per_story
total_story_points = groomed_story_points + ungroomed_story_points

# Monte Carlo Simulation
completion_sprints = []
for _ in range(simulations):
    simulated_velocity = np.random.normal(velocity, velocity_std_dev)
    simulated_velocity = max(simulated_velocity, 1)
    sprints_needed = np.ceil(total_story_points / simulated_velocity)
    completion_sprints.append(sprints_needed)

# Convert sprints to weeks
completion_times = np.array(completion_sprints) * sprint_duration_weeks

# Visualization with percentiles
percentile_90 = np.percentile(completion_times, 90)
percentile_10 = np.percentile(completion_times, 10)

plt.figure(figsize=(12, 6))
plt.hist(completion_times, bins=30, color='skyblue', edgecolor='black', alpha=0.7)
plt.axvline(np.mean(completion_times), color='red', linestyle='--', label=f"Mean: {np.mean(completion_times):.2f} weeks")
plt.axvline(percentile_10, color='green', linestyle='--', label=f"10th Percentile: {percentile_10:.2f} weeks")
plt.axvline(percentile_90, color='orange', linestyle='--', label=f"90th Percentile: {percentile_90:.2f} weeks")
plt.title("Monte Carlo Simulation: Project Completion Time", fontsize=14)
plt.xlabel("Completion Time (weeks)", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.legend()
plt.grid(alpha=0.3)
plt.show()

percentile_10, percentile_90