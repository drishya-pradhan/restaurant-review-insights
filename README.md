# Restaurant Review Insights 
An end to end data analytica dashboard that transforms raw restaurant reviews into actionable insights using sentiment analysis, rule-based theme detection, and trend analysis
---

## Problem: 
Restaurants get lots of reviews, but they are messy and time-consuming to read one-by-one. Owners often miss patterns such as 
- “Food quality dropped after menu change”
- “Slow service on certain days” 
- “Low ratings spiking this month but why”

---

## Solution: 
This project turns raw reviews into actionable and structured insights to help the restaurant understand things like: 
- What customers like the most 
- What to issues are causing negative views 
- How the ratings and complaints change over time 
This dashboard provides a clear and interactive overview of the restaurant reviews so that decisions can be made faster to improve the restaurant quality

---

## Features (MVP)

- Load restaurant reviews from a CSV file
- Data validation and cleaning
- Sentiment analysis (positive / neutral / negative)
- Rule-based theme detection (service, wait time, cleanliness, price, food quality)
- Keyword extraction
- Rating and sentiment trends over time
- Interactive Streamlit dashboard with filters and charts

---
## Tech Stack 
- Python 
- Pandas/NumPy : data processing 
- Streamlit: dashboard ui
- Vader Sentiment: lexicon based sentiment analysis 
- Git/github: version control 

--- 

## Data

The project currently uses a **sample dataset** to validate the pipeline before integrating real review sources.

### Required CSV schema

| Column     | Description |
|-----------|-------------|
| review_id | Unique identifier |
| date      | Review date (YYYY-MM-DD) |
| rating    | Integer rating (1–5) |
| text      | Review text |

Example:
```csv
review_id,date,rating,text
1,2025-11-01,5,"Amazing momo and super friendly staff!"

--- 
