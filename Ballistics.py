import pandas as pd
from pathlib import Path


class Ballistics:
    def __init__(self, csv='./ballistics.csv', min_range=-1, max_range=-1, step=-1, range_col='Range', cols=[]):
        csv_file = Path(csv)
        if csv_file.is_file():
            #print("File Found")
            self.orig_ballistics = self.ballistics = pd.read_csv(csv)

        else:
            self.orig_ballistics = self.ballistics = pd.DataFrame()

        self.range_col = range_col
        self.setrange(min_range, max_range)
        self.selectcolumns(cols)

    def setorigballistics(self, b):
        self.orig_ballistics = b

    def reset(self):
        self.ballistics = self.orig_ballistics

    def setrange(self, min_range=-1, max_range=-1, step=-1):
        min_ranges = pd.DataFrame()
        max_ranges = pd.DataFrame()
        step_ranges = pd.DataFrame()

        if max_range > 0:
            max_ranges = self.ballistics[self.range_col] <= max_range
        if min_range > 0:
            min_ranges = self.ballistics[self.range_col] >= min_range
        if step > 0:
            step_ranges = self.ballistics[self.range_col] % step == 0

        if not min_ranges.empty and not max_ranges.empty:
            self.ballistics = self.ballistics[min_ranges & max_ranges]
        elif not min_ranges.empty:
            self.ballistics = self.ballistics[min_ranges]
        elif not max_ranges.empty:
            self.ballistics = self.ballistics[max_ranges]

        if not step_ranges.empty:
            self.ballistics = self.ballistics[step_ranges]

    def selectcolumns(self, cols):
        if len(cols) > 0:
            self.ballistics = self.ballistics.iloc[:, cols]
            #print(self.ballistics.iloc[:, cols])

    def setrangecol(self, range_col):
        if range_col:
            self.range_col = range_col

    def genballisticscsv(self):
        csv_file = Path("./ballistics.csv")
        if not csv_file.is_file():
            file = open(csv_file, 'w')
            file.write('Range,Velocity,Energy,Trajectory,MOA,MILS')
            file.close()
        else:
            print("Ballistics File Exists")

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
