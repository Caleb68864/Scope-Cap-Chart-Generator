import pandas as pd
import numpy as np

df1 = pd.read_csv('./ballistics.csv')
#df2=df1.set_index("Range")
start_range = 100
end_range = 900
range_col = 'Range'
mm_col = 'Come Up (MILS)'
for index, row in df1.iterrows():
    if row[range_col] >= start_range and row[range_col] <= end_range:
        print(row[range_col], row[mm_col])
