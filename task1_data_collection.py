
import requests
import json
import os
import time
from datetime import datetime

# ---------------------------------------
# 1. API URLs and Headers
# ---------------------------------------

TOP_STORIES_URL = (
    "https://hacker-news.firebaseio.com/v0/topstories.json"
)

NEW_STORIES_URL = (
    "https://hacker-news.firebaseio.com/v0/newstories.json"
)

ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"

HEADERS = {
    "User-Agent": "TrendPulse/1.0"
}

# ---------------------------------------
# 2. Categories and Assignment Keywords
# ---------------------------------------

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


# ---------------------------------------
# 3. Fetch Story IDs
# ---------------------------------------

def fetch_story_ids(url):

    try:
        response = requests.get(
            url,
            headers=HEADERS,
            timeout=15
        )

        response.raise_for_status()

        story_ids = response.json()

        return story_ids[:500]

    except (requests.RequestException, ValueError) as error:
        print("Error fetching story IDs:", error)
        return []


# ---------------------------------------
# 4. Fetch Individual Story
# ---------------------------------------

def fetch_story(story_id):

    try:
        url = ITEM_URL.format(story_id)

        response = requests.get(
            url,
            headers=HEADERS,
            timeout=15
        )

        response.raise_for_status()

        story = response.json()

        if not story:
            return None

        if story.get("deleted") or story.get("dead"):
            return None

        if story.get("type") != "story":
            return None

        if not story.get("title"):
            return None

        return story

    except (requests.RequestException, ValueError) as error:
        print(f"Error fetching story {story_id}: {error}")
        return None


# ---------------------------------------
# 5. Collect Story Details
# ---------------------------------------

def collect_stories(story_ids):

    all_stories = []

    for index, story_id in enumerate(story_ids, start=1):

        print(f"Fetching story {index}/{len(story_ids)}")

        story = fetch_story(story_id)

        if story is not None:
            all_stories.append(story)

    return all_stories


# ---------------------------------------
# 6. Match Keywords
# ---------------------------------------

def matches_keyword(title, keywords):

    title_lower = title.lower()

    for keyword in keywords:

        if keyword.lower() in title_lower:
            return True

    return False


# ---------------------------------------
# 7. Categorize Stories
# ---------------------------------------

def categorize_stories(all_stories):

    categorized_stories = []

    assigned_story_ids = set()

    collected_at = datetime.now().astimezone().isoformat()

    for category_index, (category, keywords) in enumerate(
        categories.items()
    ):

        category_count = 0

        print(f"\nCollecting {category} stories...")

        for story in all_stories:

            if category_count >= 25:
                break

            story_id = story.get("id")
            title = story.get("title", "")

            # Avoid duplicate stories
            if story_id in assigned_story_ids:
                continue

            # Check whether the title matches a keyword
            if matches_keyword(title, keywords):

                story_data = {
                    "post_id": story_id,
                    "title": title,
                    "category": category,
                    "score": story.get("score", 0),
                    "num_comments": story.get("descendants", 0),
                    "author": story.get("by", "Unknown"),
                    "collected_at": collected_at
                }

                categorized_stories.append(story_data)

                assigned_story_ids.add(story_id)

                category_count += 1

        print(f"{category}: {category_count} stories collected")

        # Wait 2 seconds between category loops
        if category_index < len(categories) - 1:
            time.sleep(2)

    return categorized_stories


# ---------------------------------------
# 8. Main Program
# ---------------------------------------

def main():

    print("=" * 50)
    print("TRENDPULSE - DATA COLLECTION")
    print("=" * 50)

    # Fetch first 500 Top Story IDs
    print("\nFetching first 500 Top Story IDs...")

    top_story_ids = fetch_story_ids(TOP_STORIES_URL)

    print("Top story IDs fetched:", len(top_story_ids))

    # Fetch individual story details
    print("\nFetching individual story details...")

    all_stories = collect_stories(top_story_ids)

    print("\nValid stories fetched:", len(all_stories))

    # Categorize Top Stories
    print("\nStarting categorization...")

    categorized_stories = categorize_stories(all_stories)

    # Optional fallback: use only if instructor permits
    if len(categorized_stories) < 100:

        print("\nFewer than 100 stories found.")
        print("Checking additional New Stories...")

        new_story_ids = fetch_story_ids(NEW_STORIES_URL)

        existing_ids = {
            story["id"] for story in all_stories
        }

        additional_ids = [
            story_id for story_id in new_story_ids
            if story_id not in existing_ids
        ]

        additional_stories = collect_stories(additional_ids)

        all_stories.extend(additional_stories)

        categorized_stories = categorize_stories(all_stories)

    # ---------------------------------------
    # 9. Save JSON File
    # ---------------------------------------

    os.makedirs("data", exist_ok=True)

    date_string = datetime.now().strftime("%Y%m%d")

    file_name = f"data/trends_{date_string}.json"

    with open(file_name, "w", encoding="utf-8") as file:

        json.dump(
            categorized_stories,
            file,
            indent=4,
            ensure_ascii=False
        )

    # ---------------------------------------
    # 10. Display Results
    # ---------------------------------------

    print("\n" + "=" * 50)
    print("DATA COLLECTION COMPLETED")
    print("=" * 50)

    print("Total stories collected:", len(categorized_stories))

    print("Saved JSON file:", file_name)

    print("\nCategory-wise story counts:")

    for category in categories:

        count = sum(
            1 for story in categorized_stories
            if story["category"] == category
        )

        print(f"{category}: {count}")

    if len(categorized_stories) >= 100:
        print("\nSUCCESS: 100 or more stories collected.")
    else:
        print("\nWARNING: Fewer than 100 matching stories found.")


# ---------------------------------------
# 11. Run Program
# ---------------------------------------

if __name__ == "__main__":
    main()
