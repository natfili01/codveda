import os
import pandas as pd

def load_bank_data():
    """
    Load the 'bank-full.csv' dataset from the relative path.

    Returns:
        df (DataFrame): Loaded dataset
    """
    data_path = os.path.join("data", "bank-full.csv")
    df = pd.read_csv(data_path, sep=";")
    return df
