# TrendPulse – What's Actually Trending Right Now

## Project Overview

TrendPulse is a Python-based data analysis project that collects trending stories from the Hacker News API, categorizes them into different topics, processes the collected data, performs statistical analysis, and creates visualizations to understand current trends.

## Project Objectives

- Collect trending stories from Hacker News.
- Categorize stories into different topics.
- Clean and process collected data using Pandas.
- Perform statistical analysis using Pandas and NumPy.
- Visualize trends using Matplotlib.
- Identify popular stories and categories based on engagement metrics.

## Technologies Used

- Python
- Requests
- Pandas
- NumPy
- Matplotlib
- JSON
- CSV
- Hacker News API

## Project Structure

```text
Trend Plus/
│
├── task1_data_collection.py
├── task2_data_processing.py
├── task3_analysis.py
├── task4_visualization.py
├── README.md
├── .gitignore
│
├── data/
│   ├── trends_20261114.json
│   ├── trends_clean.csv
│   └── trends_analysed.csv
│
└── outputs/
    ├── chart1_top_stories.png
    ├── chart2_categories.png
    ├── chart3_scatter.png
    └── dashboard.png
```

## Tasks Completed

### Task 1 – Data Collection

- Used the Hacker News API to fetch trending story IDs.
- Collected story details using the API.
- Categorized stories into five topics:
  - Technology
  - World News
  - Sports
  - Science
  - Entertainment
- Collected story information including title, score, comments, author, and collection time.
- Saved the collected data in JSON format.

### Task 2 – Data Processing

- Loaded JSON data using Pandas.
- Removed duplicate records.
- Handled missing values.
- Processed numerical columns.
- Filtered out stories with scores below 5.
- Saved the cleaned dataset as a CSV file.

### Task 3 – Data Analysis

- Calculated average story scores.
- Calculated average number of comments.
- Calculated mean, median, and standard deviation.
- Identified maximum and minimum scores.
- Identified the category with the highest number of stories.
- Identified the most-commented story.
- Saved the analysed dataset as a CSV file.

### Task 4 – Data Visualization

Created four visualizations using Matplotlib:

- Horizontal bar chart showing the top 10 stories.
- Bar chart showing the number of stories per category.
- Scatter plot comparing story scores and comments.
- Combined TrendPulse dashboard.

## How to Run the Project

### 1. Install Required Libraries

```bash
pip install requests pandas numpy matplotlib
```

### 2. Run the Python Scripts

Execute the scripts in the following order:

```bash
python task1_data_collection.py
python task2_data_processing.py
python task3_analysis.py
python task4_visualization.py
```

## Project Results

- **104 stories collected** from Hacker News.
- **104 records** remained after duplicate and missing-value checks.
- **91 records** remained after filtering stories with scores below 5.
- Statistical analysis completed successfully.
- Four visualization files generated successfully.

## Output Files

The project generates the following outputs:

- JSON file containing collected stories.
- CSV file containing cleaned data.
- CSV file containing analysed data.
- Four visualization images stored in the `outputs/` folder.

## Data Source

Hacker News API:

https://github.com/HackerNews/API

## Conclusion

TrendPulse demonstrates an end-to-end Python data analysis workflow, starting from collecting real-time trending stories and continuing through data cleaning, statistical analysis, and visualization.

The project provides insights into trending topics, story popularity, and audience engagement using Python data analysis libraries.


