import os
import pandas as pd

def load_usa_housing_data():
    """
    Load the 'USA Housing Dataset.csv' from the relative path.

    Returns:
        df (DataFrame): Loaded housing dataset
    """
    data_path = os.path.join("data", "USA Housing Dataset.csv")
    df = pd.read_csv(data_path)
    return df
