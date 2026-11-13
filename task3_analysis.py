# Task 3: Analysis with Pandas and NumPy

import pandas as pd
import numpy as np

# Load the cleaned CSV file from Task 2
df = pd.read_csv("data/trends_clean.csv")

# Display the dataset information
print("Loaded data:", df.shape)

# Display the first 5 rows
print("\nFirst 5 rows:")
print(df.head())

# Calculate average score and average comments
average_score = df["score"].mean()
average_comments = df["num_comments"].mean()

print("\nAverage score   :", round(average_score, 2))
print("Average comments:", round(average_comments, 2))


# Basic Analysis using NumPy
print("\n--- NumPy Stats ---")

# Convert score column into a NumPy array
scores = df["score"].to_numpy()

# Calculate mean, median and standard deviation
print("Mean score   :", round(np.mean(scores), 2))
print("Median score :", round(np.median(scores), 2))
print("Std deviation:", round(np.std(scores), 2))

# Find highest and lowest scores
print("Max score    :", np.max(scores))
print("Min score    :", np.min(scores))


# Find the category with the most stories
category_counts = df["category"].value_counts()

most_category = category_counts.idxmax()
most_category_count = category_counts.max()

print(f"\nMost stories in: {most_category} ({most_category_count} stories)")


# Find the story with the most comments
most_commented = df.loc[df["num_comments"].idxmax()]

print(
    f'\nMost commented story: "{most_commented["title"]}" '
    f'— {most_commented["num_comments"]} comments'
)


# Add new columns to the DataFrame

# Engagement measures comments compared with the story score
df["engagement"] = df["num_comments"] / (df["score"] + 1)

# Mark stories as popular when their score is above average
df["is_popular"] = df["score"] > average_score


# Save the analysed DataFrame as a new CSV file
output_file = "data/trends_analysed.csv"
df.to_csv(output_file, index=False)

print(f"\nSaved to {output_file}")