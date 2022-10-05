import pandas as pd

#acquisition methods
def acquisition(path_file):
    dataframe = pd.read_csv(path_file, low_memory=False)
    return dataframe