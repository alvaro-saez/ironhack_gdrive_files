from macquisition import acquisition as ac
from mwrangling import wrangling as wr
from manalysis import analysis as an

#def main():

#DATA PIPELINE
if __name__ == "__main__":
    file_path="C:/Users/AlvaroSaez/Desktop/ironhack/dataptmad1121_lessons/module-1/datasets/vehicles.csv"
    year=[1985,1999]
    col="year"
    groupby_col="year"
    agg_col="co2"

    imported_df = ac.acquisition(file_path)
    wrangled_df = wr.wrangling(imported_df, year, col)
    analysed_df = an.analisis(wrangled_df, groupby_col, agg_col)
    print(analysed_df)