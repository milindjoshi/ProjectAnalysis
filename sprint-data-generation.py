'''
I want to generate data for the work done by 2 sprint teams. Here is the info:
1) I have 2 sprint teams. Each team has 3 resources. 
2) Sprint is of 2 weeks.
3) The 2 teams are working on the same project. There are 2 epics for this project. 
4) Team Titan is working on Front End EPIC. Team Orion is working on Back End EPIC.
5)  Front End EPIC has 75 stories where as Back End EPIC has 100 stories.
6) Both teams are working on these EPICs for 6 sprints.
7) Team Titan has completed 40 stories where as Team Orion has completed 50 stories.
8) They use Fibonacci's numbers for story points. They use 1 story point = 8 hours of work as an assumption.
9) Based on this data generate data which will show both teams sprint velocity.  
10) Based on the remaining work in the backlog, estimate how long it will take two teams to complete the work in their EPICs. 
11) Assume that some backlog items are groomed and have story point estimation. Remaining stories are ungroomed. Use the average story points from first 6 sprints to estimate the remaining ungroomed backlog work. 
12) Give step by step explanation of your understanding of what is asked and how you are generating the data for each step.
'''
import numpy as np
import math
import matplotlib.pyplot as plt

# Data for visualization
teams = ["Titan (Front End)", "Orion (Back End)"]

# Given Data
sprints_completed = 6
team_titan_completed_stories = 40
team_orion_completed_stories = 50

total_frontend_stories = 75
total_backend_stories = 100

remaining_frontend_stories = total_frontend_stories - team_titan_completed_stories
remaining_backend_stories = total_backend_stories - team_orion_completed_stories

completed_stories = [team_titan_completed_stories, team_orion_completed_stories]
remaining_stories = [remaining_frontend_stories, remaining_backend_stories]

# Fibonacci sequence (commonly used for story points): 1, 2, 3, 5, 8, 13, 21, etc.
# Assume an average Fibonacci number for completed stories.

# Simulated distribution of story points (common in agile teams)
story_point_distribution = [1, 2, 3, 5, 8]
np.random.seed(42)  # For consistent results

# Generate random story points for completed stories
titan_story_points = np.random.choice(story_point_distribution, team_titan_completed_stories)
orion_story_points = np.random.choice(story_point_distribution, team_orion_completed_stories)

# Total and Average Story Points Completed
titan_total_story_points = sum(titan_story_points)
orion_total_story_points = sum(orion_story_points)

titan_avg_velocity = titan_total_story_points / sprints_completed
orion_avg_velocity = orion_total_story_points / sprints_completed

# Assume 60% of remaining stories are groomed (common practice), rest need estimation
groomed_ratio = 0.6

groomed_frontend_stories = int(remaining_frontend_stories * groomed_ratio)
ungroomed_frontend_stories = remaining_frontend_stories - groomed_frontend_stories

groomed_backend_stories = int(remaining_backend_stories * groomed_ratio)
ungroomed_backend_stories = remaining_backend_stories - groomed_backend_stories

# Estimate ungroomed stories using average story points per completed story
titan_avg_story_points_per_story = titan_total_story_points / team_titan_completed_stories
orion_avg_story_points_per_story = orion_total_story_points / team_orion_completed_stories

estimated_frontend_story_points = groomed_frontend_stories * titan_avg_story_points_per_story + \
                                  ungroomed_frontend_stories * titan_avg_story_points_per_story

estimated_backend_story_points = groomed_backend_stories * orion_avg_story_points_per_story + \
                                 ungroomed_backend_stories * orion_avg_story_points_per_story

# Estimate remaining sprints needed
titan_remaining_sprints = estimated_frontend_story_points / titan_avg_velocity
orion_remaining_sprints = estimated_backend_story_points / orion_avg_velocity

print("Titan Velocity (Avg Story Points per Sprint):", math.ceil(titan_avg_velocity))
print("Orion Velocity (Avg Story Points per Sprint):", math.ceil(orion_avg_velocity))
print("Estimated Remaining Sprints for Titan:", math.ceil(titan_remaining_sprints))
print("Estimated Remaining Sprints for Orion:", math.ceil(orion_remaining_sprints))

# Data for updated visualization
completed_sprints = [sprints_completed, sprints_completed]
remaining_sprints = [titan_remaining_sprints, orion_remaining_sprints]

bar_width = 0.5
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# First subplot: Work Completed vs. Work Remaining
axes[0].bar(teams, completed_stories, width=bar_width, label="Completed Stories", color='green')
axes[0].bar(teams, remaining_stories, width=bar_width, bottom=completed_stories, label="Remaining Stories", color='red')
axes[0].set_ylabel("Number of Stories")
axes[0].set_title("Work Progress: Completed vs Remaining Stories")
axes[0].legend()

# Second subplot: Time Taken vs. Estimated Time Remaining
axes[1].bar(teams, completed_sprints, width=bar_width, label="Sprints Taken (Completed Work)", color='blue')
axes[1].bar(teams, remaining_sprints, width=bar_width, bottom=completed_sprints, label="Estimated Sprints Remaining", color='orange')
axes[1].set_ylabel("Number of Sprints")
axes[1].set_title("Sprint Progress: Time Spent vs Estimated Time Remaining")
axes[1].legend()

# Show the merged visualizations
plt.tight_layout()
plt.show()
