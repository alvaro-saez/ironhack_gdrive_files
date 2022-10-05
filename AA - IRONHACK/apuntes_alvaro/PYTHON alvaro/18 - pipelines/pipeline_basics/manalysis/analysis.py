import pandas as pd

#def analisis(df, groupby_col, agg_col):
#   df = df.groupby([groupby_col])[agg_col].sum()
#    return df

def analisis(df, groupby_col, agg_col):
    df = df.groupby([groupby_col])[agg_col].sum()
    df.to_csv("data/vehicles.csv")
    message = "/--------PIPELINE SUCCESSFULY EXECUTED-------/"
    return message