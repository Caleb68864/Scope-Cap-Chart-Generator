from ImageGen import ImageGen
from Ballistics import Ballistics
import wx
from GUI import FrmMain
from GUI import dlSave
from DataTable import DataTable


class Main(wx.Frame):
    def __init__(self, parent):
        FrmMain.__init__(self, parent)
        self.ballistics = Ballistics()
        self.ig = ""
        self.refresh()
        self.Show(True)

    def refresh(self,instance=None):
        if self.spinCtrl_Min_Range.GetValue() > self.spinCtrl_Max_Range.GetValue():
            self.spinCtrl_Max_Range.SetValue(self.spinCtrl_Min_Range.GetValue())

        self.ballistics.reset()
        self.ballistics.setrange(self.spinCtrl_Min_Range.GetValue(), self.spinCtrl_Max_Range.GetValue(), self.spinCtrl_Step.GetValue())
        # cols = [0, 2]
        # b.selectcolumns(cols)
        self.table = DataTable(self.ballistics.ballistics)
        self.gridBallistics.SetTable(self.table, True)
        self.gridBallistics.AutoSizeColumns()
        self.gridBallistics.AutoSizeRows()
        self.gridBallistics.Refresh()

        for column in list(self.ballistics.ballistics.columns.values):
            print(column)
            #szColCheck.Add(self.m_toggleBtn1, 0, wx.ALL, 5)

    def setstatus(self, msg):
        self.statusBar.PushStatusText(msg)

    def genimage(self):
        self.ig = ImageGen(self.ballistics.ballistics, self.setstatus)
        self.ig.setheadercolor(self.cpHeader.GetColour())
        self.ig.setrowcolor(self.cpRow.GetColour())
        self.ig.setaltrowcolor(self.cpAltRow.GetColour())
        self.ig.genimage()

    def btnPreview_Click(self, instance):
        if not self.ballistics.ballistics.empty:
            orig_size = self.imgPreview.GetSize()
            # print(orig_size)
            self.genimage()
            img = self.ig.getwximage()
            s = min(float(s) for s in orig_size)
            bmap = wx.Bitmap(self.ig.getwximage().Scale(s, s, wx.IMAGE_QUALITY_HIGH))
            self.imgPreview.SetBitmap(bmap)
            self.imgPreview.Refresh()
            self.setstatus("Preview Loaded.")
            # print("BitMap Set")
        else:
            self.setstatus("Data Empty Please Load A Ballistics File.")

        #print(self.imgPreview.GetBestSize())

    def btnExport_Click(self, instance):
        dl = dlSave(self)
        dl.btnDlSave.SetId(wx.ID_OK)
        dl.btnDlCancel.SetId(wx.ID_CANCEL)
        d = dl.ShowModal()

        if d == wx.ID_OK:
            self.genimage()
            self.ig.imgsave(dl.fpDlSave.GetPath())
            dl.Destroy()

    def btnRefresh_Click(self,instance):
        self.refresh()

    def btnClear_Click(self, instance):
        self.spinCtrl_Min_Range.SetValue(0)
        self.spinCtrl_Max_Range.SetValue(0)
        self.spinCtrl_Step.SetValue(0)
        self.m_filePicker1.SetPath("")
        self.setstatus("")
        self.ballistics = Ballistics()
        self.refresh()

    def btnReset_Click(self, instance):
        self.spinCtrl_Min_Range.SetValue(0)
        self.spinCtrl_Max_Range.SetValue(0)
        self.spinCtrl_Step.SetValue(0)
        self.setstatus("")
        self.refresh()

    def btnLoad_Click(self, instance):
        if self.m_filePicker1.GetPath() != "":
            self.ballistics = Ballistics(self.m_filePicker1.GetPath())
            self.refresh()
        else:
            print("No File Selected")
            self.setstatus("No File Selected.")

    def cbSelectAll_Click(self, instance):
        self.cbSelectNone.SetValue(False)

    def cbSelectNone_Click(self, instance):
        self.cbSelectAll.SetValue(False)


if __name__ == "__main__":
    app = wx.App(False)
    frame = Main(None)
    app.MainLoop()