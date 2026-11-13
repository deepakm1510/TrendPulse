
# TrendPulse – What's Actually Trending Right Now

## Project Overview

TrendPulse is a Python-based data analysis project that collects trending stories from Hacker News, processes the collected data, performs statistical analysis, and creates visualizations to understand current trends.

## Project Objectives

- Collect trending stories from Hacker News.
- Categorize stories into different topics.
- Clean and process the collected data using Pandas.
- Perform statistical analysis using Pandas and NumPy.
- Visualize trends using Matplotlib.

## Technologies Used

- Python
- Requests
- Pandas
- NumPy
- Matplotlib
- JSON
- CSV

## Project Structure

```text
Trend Plus/
├── task1_data_collection.py
├── task2_data_processing.py
├── task3_analysis.py
├── task4_visualization.py
├── data/
│   ├── trends_20261113.json
│   ├── trends_clean.csv
│   └── trends_analysed.csv
├── outputs/
│   ├── chart1_top_stories.png
│   ├── chart2_categories.png
│   ├── chart3_scatter.png
│   └── dashboard.png
└── README.md
```

## Tasks Completed

### Task 1 – Data Collection
- Fetched the first 500 story IDs from the Hacker News API.
- Collected stories from five categories.
- Saved the collected data in JSON format.

### Task 2 – Data Processing
- Loaded JSON data using Pandas.
- Removed duplicate records.
- Handled missing values.
- Converted numerical columns to integer format.
- Removed stories with scores below 5.
- Saved cleaned data as CSV.

### Task 3 – Data Analysis
- Calculated average score and comments.
- Calculated mean, median, and standard deviation.
- Identified maximum and minimum scores.
- Identified the category with the most stories.
- Calculated engagement and popularity indicators.
- Saved analysed data as CSV.

### Task 4 – Data Visualization
- Created a horizontal bar chart of the top 10 stories.
- Created a bar chart showing stories per category.
- Created a scatter plot comparing scores and comments.
- Created a combined TrendPulse dashboard.

## How to Run the Project

Install the required libraries:

```bash
pip install requests pandas numpy matplotlib
```

Run the Python files in this order:

```bash
python task1_data_collection.py
python task2_data_processing.py
python task3_analysis.py
python task4_visualization.py
```

## Output

The project generates:

- JSON file containing collected stories.
- CSV file containing cleaned data.
- CSV file containing analysed data.
- Four visualization images in the outputs folder.

## Data Source

Hacker News API: https://github.com/HackerNews/API

## Conclusion

TrendPulse demonstrates a complete Python data analysis workflow, from collecting real-time trending stories to processing, analysing, and visualizing the data.
