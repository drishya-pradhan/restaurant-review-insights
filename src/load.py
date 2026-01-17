import pandas as pd
COLUMNS = {"review_id", "date", "rating", "text"}  #constant
def loadReviews(csvpath: str) -> pd.DataFrame: 
    """
    Load reviews.csv and validate required columns 
    
    :param csvpath: takes in a csv file
    :type csvpath: str
    :return: outputs a pandas dataframe
    :rtype: DataFrame
    """
    df = pd.read_csv(csvpath)
    # set(df.columns) = df.columns -> makes the list objects of column names
    # set(df.columns) -> converts it to a set 
    missing = COLUMNS - set(df.columns) # contains whats wrong or missing in the csv given
    if missing: 
        raise ValueError(f"Missing Required Columns: {sorted(missing)}")
    return df 