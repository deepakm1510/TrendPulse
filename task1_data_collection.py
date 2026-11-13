
# Task 1: TrendPulse - Data Collection

# Import required libraries
import requests
import json
import os
import time
from datetime import datetime

# Hacker News API URLs
TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"

# Required User-Agent header
headers = {
    "User-Agent": "TrendPulse/1.0"
}

# Categories and their keywords
categories = {
    "technology": [
        "AI", "software", "tech", "code", "computer",
        "data", "cloud", "API", "GPU", "LLM"
    ],
    "worldnews": [
        "war", "government", "country", "president",
        "election", "climate", "attack", "global"
    ],
    "sports": [
        "NFL", "NBA", "FIFA", "sport", "game",
        "team", "player", "league", "championship"
    ],
    "science": [
        "research", "study", "space", "physics",
        "biology", "discovery", "NASA", "genome"
    ],
    "entertainment": [
        "movie", "film", "music", "Netflix", "game",
        "book", "show", "award", "streaming"
    ]
}

# Maximum stories to collect in each category
MAX_STORIES_PER_CATEGORY = 25

# Fetch the top 500 story IDs from Hacker News
try:
    response = requests.get(
        TOP_STORIES_URL,
        headers=headers,
        timeout=15
    )
    response.raise_for_status()

    story_ids = response.json()[:500]
    print(f"Successfully fetched {len(story_ids)} story IDs.")

except requests.RequestException as error:
    print(f"Error fetching top stories: {error}")
    story_ids = []

# Fetch story details and store them for category processing
all_stories = []

for story_id in story_ids:
    try:
        story_response = requests.get(
            ITEM_URL.format(story_id),
            headers=headers,
            timeout=15
        )
        story_response.raise_for_status()

        story = story_response.json()

        # Skip deleted, missing, or invalid stories
        if not story or story.get("type") != "story":
            continue

        title = story.get("title", "")

        if not title:
            continue

        all_stories.append(story)

    except requests.RequestException as error:
        print(f"Error fetching story {story_id}: {error}")
        continue

# Store collected stories
collected_stories = []

# Keep track of stories already assigned to a category
assigned_story_ids = set()

# Process each category separately
for category, keywords in categories.items():

    category_count = 0

    print(f"\nCollecting {category} stories...")

    for story in all_stories:

        # Stop when the category reaches its limit
        if category_count >= MAX_STORIES_PER_CATEGORY:
            break

        story_id = story.get("id")

        # Avoid assigning the same story to multiple categories
        if story_id in assigned_story_ids:
            continue

        title = story.get("title", "")
        title_lower = title.lower()

        # Check keywords without case sensitivity
        if any(keyword.lower() in title_lower for keyword in keywords):

            collected_stories.append({
                "post_id": story_id,
                "title": title,
                "category": category,
                "score": story.get("score", 0),
                "num_comments": story.get("descendants", 0),
                "author": story.get("by", "Unknown"),
                "collected_at": datetime.now().isoformat()
            })

            assigned_story_ids.add(story_id)
            category_count += 1

    print(f"{category}: {category_count} stories collected.")

    # Wait 2 seconds between category loops
    if category != list(categories.keys())[-1]:
        time.sleep(2)

# Create the data folder
os.makedirs("data", exist_ok=True)

# Save collected stories as JSON
filename = f"data/trends_{datetime.now().strftime('%Y%m%d')}.json"

with open(filename, "w", encoding="utf-8") as file:
    json.dump(
        collected_stories,
        file,
        indent=4,
        ensure_ascii=False
    )

# Print collection summary
print("\nData collection completed!")
print(f"Total stories collected: {len(collected_stories)}")
print(f"Saved file: {filename}")
