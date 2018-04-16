from ImageGen import ImageGen
from Ballistics import Ballistics
import wx
from GUI import FrmMain
from DataTable import DataTable


class Main(wx.Frame):
    def __init__(self, parent):
        FrmMain.__init__(self, parent)
        self.refresh()
        self.Show(True)

    def refresh(self,instance=None):
        self.ballistics = Ballistics()
        self.ballistics.setrange(self.spinCtrl_Min_Range.GetValue(), self.spinCtrl_Max_Range.GetValue())
        # cols = [0, 2]
        # b.selectcolumns(cols)
        self.table = DataTable(self.ballistics.ballistics)
        self.gridBallistics.SetTable(self.table, True)
        self.gridBallistics.AutoSizeColumns()
        self.gridBallistics.AutoSizeRows()

    def btnPreview_Click(self, instance):
        orig_size = self.imgPreview.GetSize()
        print(orig_size)
        ig = ImageGen(self.ballistics.ballistics)
        img = ig.getwximage()
        s = min(float(s) for s in orig_size)
        bmap = wx.Bitmap(ig.getwximage().Scale(s, s, wx.IMAGE_QUALITY_HIGH))
        self.imgPreview.SetBitmap(bmap)
        self.imgPreview.SetSize(orig_size)
        #print("BitMap Set")
        #self.imgPreview.SetSize(orig_size)
        #print(self.imgPreview.GetBestSize())

    def btnExport_Click(self, instance):
        ig = ImageGen(self.ballistics.ballistics)
        ig.imgsave()

    def btnRefresh_Click(self,instance):
        self.refresh()

    def btnClear_Click(self, instance):
        self.spinCtrl_Min_Range.SetValue(0)
        self.spinCtrl_Max_Range.SetValue(0)
        self.refresh()

if __name__ == "__main__":
    app = wx.App(False)
    frame = Main(None)
    app.MainLoop()