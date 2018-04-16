import numpy as np
import pandas as pd
import wx
import wx.grid


EVEN_ROW_COLOUR = '#CCE6FF'
GRID_LINE_COLOUR = '#ccc'

class DataTable(wx.grid.GridTableBase):

    def __init__(self, data=None):
        wx.grid.GridTableBase.__init__(self)
        self.headerRows = 0
        if data is None:
            data = pd.DataFrame()
        self.data = data

    def GetNumberRows(self):
        return len(self.data)

    def GetNumberCols(self):
        return len(self.data.columns)

    def GetValue(self, row, col):
        # if col == 0:
        #     return self.data.index[row]
        return self.data.iloc[row, col]

    def SetValue(self, row, col, value):
        self.data.iloc[row, col] = value

    def GetColLabelValue(self, col):
        return self.data.columns[col]

    def GetTypeName(self, row, col):
        return wx.grid.GRID_VALUE_STRING

    def GetAttr(self, row, col, prop):
        attr = wx.grid.GridCellAttr()
        if row % 2 == 1:
            attr.SetBackgroundColour(EVEN_ROW_COLOUR)
        return attr