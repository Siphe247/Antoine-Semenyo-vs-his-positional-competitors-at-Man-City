import matplotlib.pyplot as plt
import numpy as np
from highlight_text import fig_text
from PIL import Image

# This is a horizontal bar chart of their Passing Stats per 90 on FBREF. 
# Looking at their goals, assists, progressive (carries, passes and passes received).

# Players
players = ['Antoine Semenyo', 'Phil Foden', 'Jérémy Doku', 'Rayan Cherki', 'Savinho']

# FBREF Dataset
total_passes_completed= [21.1,46.6,31.4,56.3,37.8]
total_pass_completion_percentage = [68.8,82.5,79.2,81.7,79.4]
progressive_passing_distance=[96.2,172.6,123.8,198.3,91.3]
short_pass_completion_percentage = [82.7,92.2,84.6,88.5,87.5]
medium_pass_completion_percentage = [70.6,86.1,80.1,87.5,82.4]
long_pass_completion_percentage = [43.0,52.5,64.0,38.8,56.3]

# Setting up the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Player faces
player_faces = {
    'Antoine Semenyo': ('/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Antoine Semenyo/Semenyo.png'),
    'Phil Foden': ('/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Antoine Semenyo/Foden.png'),
    'Jérémy Doku': ('/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Antoine Semenyo/Doku.png'),
    'Rayan Cherki': ('/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Antoine Semenyo/Cherki.png'),
    'Savinho': ('/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Antoine Semenyo/Savinho.png')
}

# Set the width of bars and positions
bar_height = 0.15  # Bar height for 5 bars
y_pos = np.arange(len(players))

# Create bars for each stat - FIXED: Evenly spaced bars
bars1 = ax.barh(y_pos - 2*bar_height, total_passes_completed, bar_height, 
                label='Total Passes Completed', color="#ff0000", alpha=0.85)
bars2 = ax.barh(y_pos - 1*bar_height, total_pass_completion_percentage, bar_height, 
                label='Total Pass Completion %', color="#005f9e", alpha=0.85)
bars3 = ax.barh(y_pos, progressive_passing_distance, bar_height, 
                label='Progressive Passing Distance (in Yds)', color="#eb00b87a", alpha=0.85)
bars4 = ax.barh(y_pos + 1*bar_height, short_pass_completion_percentage, bar_height, 
                label='Short Pass Completion %', color="#00eaff", alpha=0.85)
bars5 = ax.barh(y_pos + 2*bar_height, long_pass_completion_percentage, bar_height, 
                label='Long Pass Completion %', color="#f88400", alpha=0.85)

background_color = "#000000"

# Add value labels on bars
for bars in [bars1, bars2, bars3, bars4, bars5]:
    for bar in bars:
        width = bar.get_width()
        # Format full_games_played with decimal, others as integers
        if bars == bars2:
            label = f'{width:.1f}'
        else:
            label = f'{int(width)}'
        ax.text(width + 2, bar.get_y() + bar.get_height()/2, 
                label,
                ha='left', va='center', fontsize=10, fontweight='bold')

# Customize the plot
ax.set_yticks(y_pos)
ax.set_yticklabels(players, fontsize=13, fontweight='bold')

# Adjust the main plot position to make room for player images
fig.subplots_adjust(left=0.22)

# Add player faces to the left of player names
for i, player in enumerate(players):
    try:
        img = Image.open(player_faces[player])
        # Create a small axes for each player image
        imagebox = fig.add_axes([0.039, 0.15 + i*0.155, 0.05, 0.12])
        imagebox.imshow(img)
        imagebox.axis('off')
    except FileNotFoundError:
        print(f"Image not found for {player}")
    except Exception as e:
        print(f"Error loading image for {player}: {e}")

ax.set_xlabel('Value', fontsize=13, fontweight='bold')
ax.set_title("Manchester City's Winger Premier League Passing Per 90 Stats 2025/26", 
             fontsize=16, fontweight='bold', pad=20)

# Add legend
ax.legend(loc='upper right', fontsize=11, framealpha=0.9)

# Add grid
ax.grid(axis='x', alpha=0.3, linestyle='--')
ax.set_axisbelow(True)

# Remove top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Set x-axis limit
max_value = max(max(total_passes_completed), max(total_pass_completion_percentage), 
                max(progressive_passing_distance), max(short_pass_completion_percentage), max(long_pass_completion_percentage))
ax.set_xlim(0, max_value * 1.12)

# Premier league badge
ax7 = fig.add_axes([0.01, 0.89, 0.15, 0.13])
ax7.axis('off')
img = Image.open('/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Premier_League_Logo.png')
ax7.imshow(img)

# Manchester City badge
ax8 = fig.add_axes([0.88, 0.89, .15, .13])
ax8.axis('off')
img = Image.open('/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Prem 25:26 club badges/Manchester City_logo.png')
ax8.imshow(img)

# Add credits BEFORE plt.show() and plt.savefig()
CREDIT_1 = "Data: FBREF"
CREDIT_2 = "Viz: Siphe247"

fig_text(
    0.99, 0.02, f"{CREDIT_1}\n{CREDIT_2}", size=12,
    color="#000000",
    ha="right", va="bottom"
)

# Save the figure BEFORE plt.show()
plt.savefig('/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Antoine Semenyo/Manchester City Winger Passing Stats 2025-26.png', 
            dpi=300, bbox_inches='tight', facecolor='white')
print("Figure saved successfully!")

# Show the plot
plt.show()