
# Task 4: Visualizations using Matplotlib
# TrendPulse - What's Actually Trending Right Now

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Load the analysed data from Task 3
df = pd.read_csv("data/trends_analysed.csv")

# Create the outputs folder if it does not exist
output_folder = Path("outputs")
output_folder.mkdir(exist_ok=True)

print("Loaded data:", df.shape)


# Chart 1: Top 10 Stories by Score

top_stories = df.nlargest(10, "score").copy()

# Shorten story titles to a maximum of 50 characters
short_titles = top_stories["title"].apply(
    lambda title: title[:47] + "..." if len(title) > 50 else title
)

plt.figure(figsize=(12, 7))
plt.barh(short_titles, top_stories["score"])
plt.xlabel("Score")
plt.ylabel("Story Title")
plt.title("Top 10 Stories by Score")
plt.gca().invert_yaxis()
plt.tight_layout()

# Save chart before closing it
plt.savefig(output_folder / "chart1_top_stories.png", dpi=300)
plt.close()


# Chart 2: Stories per Category

category_counts = df["category"].value_counts()

plt.figure(figsize=(10, 6))
plt.bar(
    category_counts.index,
    category_counts.values,
    color=["skyblue", "orange", "lightgreen", "salmon", "purple"]
)
plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.title("Number of Stories per Category")
plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig(output_folder / "chart2_categories.png", dpi=300)
plt.close()


# Chart 3: Score vs Comments

popular = df[df["is_popular"] == True]
not_popular = df[df["is_popular"] == False]

plt.figure(figsize=(10, 6))

plt.scatter(
    not_popular["score"],
    not_popular["num_comments"],
    color="orange",
    label="Not Popular",
    alpha=0.7
)

plt.scatter(
    popular["score"],
    popular["num_comments"],
    color="green",
    label="Popular",
    alpha=0.7
)

plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.title("Score vs Comments")
plt.legend()
plt.tight_layout()

plt.savefig(output_folder / "chart3_scatter.png", dpi=300)
plt.close()


# Bonus: Combined TrendPulse Dashboard

fig, axes = plt.subplots(1, 3, figsize=(20, 7))

# Dashboard Chart 1: Top 10 stories
axes[0].barh(short_titles, top_stories["score"])
axes[0].set_xlabel("Score")
axes[0].set_ylabel("Story Title")
axes[0].set_title("Top 10 Stories")
axes[0].invert_yaxis()

# Dashboard Chart 2: Stories per category
axes[1].bar(
    category_counts.index,
    category_counts.values,
    color=["skyblue", "orange", "lightgreen", "salmon", "purple"]
)
axes[1].set_xlabel("Category")
axes[1].set_ylabel("Number of Stories")
axes[1].set_title("Stories per Category")
axes[1].tick_params(axis="x", rotation=45)

# Dashboard Chart 3: Score vs Comments
axes[2].scatter(
    not_popular["score"],
    not_popular["num_comments"],
    color="orange",
    label="Not Popular",
    alpha=0.7
)
axes[2].scatter(
    popular["score"],
    popular["num_comments"],
    color="green",
    label="Popular",
    alpha=0.7
)
axes[2].set_xlabel("Score")
axes[2].set_ylabel("Number of Comments")
axes[2].set_title("Score vs Comments")
axes[2].legend()

# Add dashboard title
fig.suptitle("TrendPulse Dashboard", fontsize=18)
fig.tight_layout(rect=[0, 0, 1, 0.93])

# Save dashboard
plt.savefig(output_folder / "dashboard.png", dpi=300)
plt.close()

print("\nAll visualizations completed successfully!")
print("\nSaved chart files in the outputs folder:")
print("- chart1_top_stories.png")
print("- chart2_categories.png")
print("- chart3_scatter.png")
print("- dashboard.png")
