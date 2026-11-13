# Task 2: Clean the Data and Save as CSV

import pandas as pd
from pathlib import Path

# Find the latest JSON file created by Task 1
data_folder = Path("data")

json_files = sorted(
    data_folder.glob("trends_*.json"),
    key=lambda file: file.stat().st_mtime,
    reverse=True
)

if not json_files:
    raise FileNotFoundError("No JSON file found in the data folder.")

input_file = json_files[0]

# Load JSON data into a Pandas DataFrame
df = pd.read_json(input_file)

print(f"Loaded {len(df)} stories from {input_file}")

# Remove duplicate stories using post_id
df = df.drop_duplicates(subset="post_id", keep="first")
print(f"After removing duplicates: {len(df)}")

# Remove extra spaces from titles
df["title"] = df["title"].astype("string").str.strip()

# Convert score and num_comments into numeric values
df["score"] = pd.to_numeric(df["score"], errors="coerce")
df["num_comments"] = pd.to_numeric(df["num_comments"], errors="coerce")

# Treat empty titles as missing values
df["title"] = df["title"].replace("", pd.NA)

# Remove rows missing post_id, title, or score
df = df.dropna(subset=["post_id", "title", "score"])
print(f"After removing nulls: {len(df)}")

# Fill missing comment counts with 0
df["num_comments"] = df["num_comments"].fillna(0)

# Convert score and num_comments to integers
df["score"] = df["score"].astype(int)
df["num_comments"] = df["num_comments"].astype(int)

# Remove stories with a score below 5
df = df[df["score"] >= 5].copy()
print(f"After removing low scores: {len(df)}")

# Save the cleaned data as a CSV file
output_file = data_folder / "trends_clean.csv"
df.to_csv(output_file, index=False)

print(f"\nSaved {len(df)} rows to {output_file}")

# Display the number of stories in each category
print("\nStories per category:")
print(df["category"].value_counts().to_string())