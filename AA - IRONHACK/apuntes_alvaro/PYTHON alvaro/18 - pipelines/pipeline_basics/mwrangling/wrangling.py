import pandas as pd

def wrangling(df, year, col): #year should be an integer and col a string
    df = df[df[col].isin(year)]
    return df