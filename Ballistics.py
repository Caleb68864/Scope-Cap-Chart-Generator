import pandas as pd

class Ballistics:
    def __init__(self):
        pass

    def getballistics(self):
        df1 = pd.read_csv('./ballistics.csv')
        # df2=df1.set_index("Range")
        start_range = 100
        end_range = 500
        range_col = 'Range'
        mm_col = 'Come Up (MILS)'

        # for index, row in df1.iterrows():
        #     if row[range_col] >= start_range and row[range_col] <= end_range:
        #         print(row[range_col], row[mm_col])

        return df1