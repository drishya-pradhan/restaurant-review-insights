import streamlit as st
#importing needed functions
from src.load import loadReviews
from src.clean import cleanReviews

st.set_page_config (
    page_title= "Review Insights", # fo the page title in browser tab
    page_icon= ":bar_chart:", 
    layout= "wide", # use entire screen 
)
st.title("Restaurant Reviews Insights Dashboard :bar_chart:")
DATAPATH = "data/reviews.csv"

st.header("Load and Validate Data")
try: 
    rawdf = loadReviews(DATAPATH)
    st.success(f"Loaded {len(rawdf)} rows from {DATAPATH}")
except Exception as e: 
    st.error(f"Failed to load data: {e}")
    st.stop()

st.header("Clean Data")
cleandf = cleanReviews(rawdf)
st.success(f"After cleaning: {len(cleandf)} rows")

#Summary Metrics 
st.header("Dataset Overview")
# create columns so metrics appear side by side 
col1, col2, col3 = st.columns(3)

# tells how many valid reviews we have after cleaning
col1.metric("Total Reviews", len(cleandf))

# shows the average rating and confirms ratings are numeric 
col2.metric("Average Rating: ", round(cleandf["rating"].mean(), 2))

# show how many reviews actually have text in %
col3.metric("Reviews with Text (%)", 
            round(cleandf["hasText"].mean() *100, 1))

# confirms when the time frame of reviews in the dataset 
st.subheader("Date Range")
st.write( 
    f"{cleandf['date'].min().date()} -> {cleandf['date'].max().date()}"
)

# shows missing values before cleaning so i can see og data quality
st.subheader("Missing Values - Raw ") 
st.write(rawdf.isna().sum())

# shows how ratings are distributed from 1 to 5 
st.subheader("Rating Distribution - Cleaned data")
st.write(cleandf["rating"].value_counts().sort_index())

# preview table
st.subheader("Cleaned Data Preview")
st.dataframe(cleandf.head(17))
