import pandas as pd

def convert_to_categorical(df, column):
    
    # Check if the specified column exists in the dataframe
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in the dataframe.")

    # Convert the specified column to categorical
    df[column] = df[column].astype('category')

    return df
