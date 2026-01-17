import pandas as pd 
def cleanReviews(df: pd.DataFrame) -> pd.DataFrame: 
    clean = df.copy()

    clean["date"] = pd.to_datetime(clean["date"], errors = "coerce")
   
   # converts ratings to real numbers or NaN and keeps only rows with valid ratings (1 to 5)
    clean["rating"] = pd.to_numeric(clean["rating"], errors = "coerce")
    clean = clean[clean["rating"].between(1,5)]

    # forces column to be string and if text is missing => becomes empty string 
    clean["text"] = clean["text"].fillna("").astype(str)
    
    # replaces messy whitespace or newlines with a single space 
    clean["text"] = clean["text"].str.replace(r"\s+", " ", regex=True).str.strip()

    # Derived fields 
    clean["textLength"] = clean["text"].str.len()
    clean["hasText"] = clean["textLength"] > 0
    
    # invalid dates that we got from errors = "coerce" is dropped so that trend chards dont break
    clean = clean.dropna(subset = ["date"])
    
    # converts each date in to yyyy-mm bucket; good for average rating per month ccharts 
    clean["month"] = clean["date"].dt.to_period("M").astype(str)
    return clean



